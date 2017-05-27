def inputeval(input_string):
    return input_string.split()


def unitConvert(value, origUnit, ConvertToUnit):

    unitConversionTable = {
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

    if origUnit in unitConversionTable:
        value = float(value)
        return (value
                * unitConversionTable[orig_unit]
                / unitConversionTable[ConvertToUnit])
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
