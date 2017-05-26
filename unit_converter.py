def inputeval(input_string):
    user_input = input_string.split()
    number = user_input[0]
    initial_unit = user_input[1]
    convert_to_unit = user_input[2]

    return (number, initial_unit, convert_to_unit)


def unitConvert(value, origUnit, ConvertToUnit):

    originalUnitToKiloMeter = {
            "mm": 1 / 1000000,
            "cm": 1 / 100000,
            "dm": 1 / 10000,
            "m": 1 / 1000,
            "km": 1,
            "in": 1 / 100000 * 2.54,
            "ft": 1 / 100000 * 2.54 * 12,
            "yd": 1 / 100000 * 2.54 * 12 * 3,
            "mi": 1 / 0.621371
            }

    unitRebased = originalUnitToKiloMeter[origUnit]

    convertTo = {
            "mm": unitRebased * 1000000,
            "cm": unitRebased * 100000,
            "dm": unitRebased * 10000,
            "m": unitRebased * 1000,
            "km": unitRebased,
            "in": unitRebased * 12 * 5280 * 0.621371,
            "mi": unitRebased * 0.621371,
            "ft": unitRebased * 5280 * 0.621371,
            "yd": unitRebased * 0.623171 * 1760
            }

    if origUnit in originalUnitToKiloMeter:
        value = float(value)
        return value * convertTo[ConvertToUnit]
    else:
        return "Invalid unit conversion"


print("Unit converter usage.  1 km cm")
print("Result:  1 km is 100 cm")
print("conversions supported: mm, cm, dm, m, mi, ft, yd, in")

while(True):
    print("> ", end="")
    user_conversion_request = input()
    if (user_conversion_request in {"exit", "quit"}):
        break

    unit_value, orig_unit, convert_unit = inputeval(user_conversion_request)

    print(unit_value, orig_unit, "is",
          unitConvert(unit_value, orig_unit, convert_unit),
          str(convert_unit))
