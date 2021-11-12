def _determine_cooling_needs(current_mode, cooling_setpoint, temp, buffer):
    new_mode = "null"
    message = ""

    # If not cooling, determine if cooling is needed
    if current_mode != "Cool" and temp > cooling_setpoint:
        new_mode = "Cool"
        message = f"{temp} is above cooling setpoint {cooling_setpoint}, initiating cooling"

    # If cooling and temp is below the cooling setpoint, see if temp is below the setpoint minus buffer
    elif current_mode == "Cool" and temp > (cooling_setpoint - buffer):
        new_mode = "Cool"
        message = f"temperature of {temp} requires more cooling"

    # If temp is below the setpoint minus buffer, stop cooling
    elif current_mode == "Cool" and (cooling_setpoint - buffer) > temp:
        new_mode = "Do_Nothing"
        message = f"temperature of {temp} is low enough to halt cooling"

    return new_mode, message


def _determine_heating_needs(current_mode, heating_setpoint, temp, buffer):
    new_mode = "null"
    message = ""

    # If not heating, determine if heating is needed
    if current_mode != "Heat" and heating_setpoint > temp:
        new_mode = "Heat"
        message = f"{temp} is below heating setpoint {heating_setpoint}, initiating heating"

    # If heating and temp is above the heating setpoint, see if temp is above the setpoint plus buffer
    elif current_mode == "Heat" and (heating_setpoint + buffer) > temp:
        new_mode = "Heat"
        message = f"temperature of {temp} requires more heating"

    # If temp is above setpoint plus buffer, stop heating
    elif current_mode == "Heat" and temp > (heating_setpoint + buffer):
        new_mode = "Do_Nothing"
        message = f"temperature of {temp} is low enough to halt heating"

    return new_mode, message


def determine_hvac_needs(current_mode, heating_setpoint, cooling_setpoint, temp, buffer):
    new_mode, message = _determine_cooling_needs(current_mode, cooling_setpoint, temp, buffer)
    if new_mode == "null":
        new_mode, message = _determine_heating_needs(current_mode, heating_setpoint, temp, buffer)
        if new_mode == "null":
            new_mode = "Do_Nothing"
            message = f"temperature of {temp} requires no action"

    return new_mode, message
