import random

from Data_Helpers import HVAC


# -------------------------------------
#
#  Test cooling functionality from "Do Nothing"
#
# -------------------------------------

def test_cooling_start_recognized():
    for i in range(1000):
        current_mode = 'Do_Nothing'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = cooling_setpoint_c + random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode == 'Cool'


def test_cooling_continued():
    for i in range(1000):
        current_mode = 'Cool'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = cooling_setpoint_c - setpoint_buffer_c + random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode == 'Cool'


def test_cooling_stopped():
    for i in range(1000):
        current_mode = 'Cool'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = cooling_setpoint_c - setpoint_buffer_c - random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode != 'Cool'

# -------------------------------------
#
#  Test heating functionality from "Do Nothing"
#
# -------------------------------------


def test_heating_start_recognized():
    for i in range(1000):
        current_mode = 'Do_Nothing'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = heating_setpoint_c - random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode == 'Heat'


def test_heating_continued():
    for i in range(1000):
        current_mode = 'Heat'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = heating_setpoint_c + setpoint_buffer_c - random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode == 'Heat'


def test_heating_stopped():
    for i in range(1000):
        current_mode = 'Heat'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = heating_setpoint_c + setpoint_buffer_c + random.uniform(0.01, 10)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode != 'Heat'

# -------------------------------------
#
#  Test no action functionality from "Do Nothing"
#
# -------------------------------------


def test_continued_do_nothing():
    for i in range(1000):
        current_mode = 'Do_Nothing'
        middle_of_deadband = 23
        cooling_setpoint_c = random.uniform(middle_of_deadband, middle_of_deadband + 5)
        heating_setpoint_c = random.uniform(middle_of_deadband - 5, middle_of_deadband)
        setpoint_buffer_c = 0.15
        temperature = random.uniform(heating_setpoint_c, cooling_setpoint_c)
        new_mode, message = HVAC.determine_hvac_needs(current_mode, heating_setpoint_c, cooling_setpoint_c, temperature, setpoint_buffer_c)
        assert new_mode == 'Do_Nothing'
