import time
import yaml
import math

from External_Utilities import get_time
from Data_Helpers import House, HVAC, Schedule
from External_Utilities import Text_Alerting

# --------------------------------------------
#
# Initialization
#
# --------------------------------------------

# Send command - set to false for testing
send_command = True

# Create a config object based on the config file
with open('Configuration/config.yml') as c:
    config = yaml.load(c, Loader=yaml.FullLoader)

# Create house and set initial mode
house = House.House(config)
mode = 3  # set initial mode

# Initialize alerting trackers
failed_loop_counter = 0  # keep track of how many times in a row the loop has failed
last_alert_sent = -math.inf
initialization_time = get_time.now(config)

# --------------------------------------------
#
# Command Run Loop
#
# --------------------------------------------

while True:
    try:

        # Get time, room schedule, and setpoints
        current_hour = get_time.now(config).hour
        control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c = \
            Schedule.get_current_schedule(config, current_hour)

        # Get sensor data
        for room in house.rooms:
            if room.name == control_room:
                temperature = room.temp

        # Print an update to logs
        now = get_time.now(config)
        runtime = (now - initialization_time)
        runtime_hours = round(runtime.total_seconds()/60/60, 2)
        print("-------------------------------------------------------------------------------")
        print(f"Time {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}  |  "
              f"Room = {control_room}    ",
              f"Hour = {current_hour}    ",
              f"Setpoints = {heating_setpoint_c} - {cooling_setpoint_c}    ",
              f"Temp = {temperature}    ",
              f"Uninterrupted Runtime = {runtime_hours} Hours"
              )

        # Determine command and message
        mode, message = HVAC.determine_hvac_needs(
            current_mode=mode,
            heating_setpoint=heating_setpoint_c,
            cooling_setpoint=cooling_setpoint_c,
            temp=temperature,
            buffer=setpoint_buffer_c
        )
        print(message)
        print("-------------------------------------------------------------------------------")

        # Send command to thermostat
        if send_command:
            house.send_command_to_thermostat(mode)
        else:
            print("no command sent, change configuration to have commands sent to thermostat")

        # Check if we should notify that the script has resumed
        min_alerting_threshold = config['ALERTING']['min_alerting_threshold']
        if failed_loop_counter >= min_alerting_threshold:
            Text_Alerting.TwilioClient().send_loop_resume_text()
            print("Sent Resume Operation Text")

        # If the command was successfully sent, reset the failed loop counter
        failed_loop_counter = 0

        # Sleep until next loop iteration
        time.sleep(config['COMMAND_OPTIONS']['command_frequency_secs'])

    except:
        # Iterate failed loop counter
        failed_loop_counter += 1

        # Restart time for "Uninterrupted Runtime"
        initialization_time = get_time.now(config)

        # Print a warning message to the logs
        print(f"**** An error occurred (ct={failed_loop_counter}) "
              f"- I was likely unable to connect to devices - sleeping and restarting loop ****")

        # Check if an alert should be sent
        min_alerting_threshold = config['ALERTING']['min_alerting_threshold']
        max_alerting_freq_secs = config['ALERTING']['max_alerting_frequency_hrs']*60*60

        enough_failures_to_trigger = (failed_loop_counter >= min_alerting_threshold)
        long_enough_since_last_alert = time.time() > (last_alert_sent + max_alerting_freq_secs)

        # If conditions are met, send an alert
        if enough_failures_to_trigger and long_enough_since_last_alert:
            Text_Alerting.TwilioClient().send_failed_loop_text(failed_loop_counter)
            print("Sent Alert Text")
            last_alert_sent = time.time()

        # Sleep for an shorter than normal time, then try again
        time.sleep(config['COMMAND_OPTIONS']['command_frequency_secs'])

