from External_Utilities.Google_Sheets_API import get_schedule_df


# def get_current_schedule(config, hour):
#     # get room schedule and setpoints for current time
#     for potential_schedule in config['SCHEDULES']:
#         first_hour = config['SCHEDULES'][potential_schedule]['first_hour']
#         last_hour = config['SCHEDULES'][potential_schedule]['last_hour']
#         if first_hour < last_hour:
#             if first_hour <= hour <= last_hour:
#                 schedule = potential_schedule
#         elif first_hour > last_hour:
#             if hour >= first_hour or hour <= last_hour:
#                 schedule = potential_schedule
#
#     # Control parameters for the current time
#     control_room = config['SCHEDULES'][schedule]['control_sensor']
#     heating_setpoint_c = config['SCHEDULES'][schedule]["heating_setpoint"]
#     cooling_setpoint_c = config['SCHEDULES'][schedule]["cooling_setpoint"]
#     setpoint_buffer_c = config['SETPOINT_OPTIONS']['setpoint_buffer_c']
#
#     return control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c


def get_current_schedule(config, hour):
    sheet_id = '11zDZeqEYe1OJ8z154Tcms0AD6wazsSEz2qdpq9BEtM8'

    schedule_df = get_schedule_df(sheet_id)

    # get room schedule and setpoint for current time
    for index, row in schedule_df.iterrows():
        first_hour = row['first_hour']
        last_hour = row['last_hour']

        if first_hour < last_hour:
            if first_hour <= hour <= last_hour:
                schedule = row
        elif first_hour > last_hour:
            if hour >= first_hour or hour <= last_hour:
                schedule = row

    # Control parameters for the current time
    control_room = schedule['control_sensor']
    heating_setpoint_c = schedule["heating_setpoint"]
    cooling_setpoint_c = schedule["cooling_setpoint"]
    setpoint_buffer_c = config['SETPOINT_OPTIONS']['setpoint_buffer_c']

    return control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c
