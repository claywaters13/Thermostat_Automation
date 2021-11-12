import yaml

from Data_Helpers import Schedule

# -------------------------------------
#
#  Test what the schedule returns
#
# -------------------------------------


def test_schedule_sensor():
    with open('Configuration/config.yml') as c:
        config = yaml.load(c, Loader=yaml.FullLoader)
    for i in range(1000):
        hour = i % 24
        control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c = \
            Schedule.get_current_schedule(config, hour)

        assert control_room == 'Main' or control_room == 'Bedroom'


def test_schedule_heating_setpoint():
    with open('Configuration/config.yml') as c:
        config = yaml.load(c, Loader=yaml.FullLoader)
    for i in range(1000):
        hour = i % 24
        control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c = \
            Schedule.get_current_schedule(config, hour)

        assert 10 < heating_setpoint_c < 30


def test_schedule_cooling_setpoint():
    with open('Configuration/config.yml') as c:
        config = yaml.load(c, Loader=yaml.FullLoader)
    for i in range(1000):
        hour = i % 24
        control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c = \
            Schedule.get_current_schedule(config, hour)

        assert 10 < cooling_setpoint_c < 30


def test_schedule_setpoint_buffer():
    with open('Configuration/config.yml') as c:
        config = yaml.load(c, Loader=yaml.FullLoader)
    for i in range(1000):
        hour = i % 24
        control_room, heating_setpoint_c, cooling_setpoint_c, setpoint_buffer_c = \
            Schedule.get_current_schedule(config, hour)

        assert 0 < setpoint_buffer_c < 5