
def inputeval(input_string):
    user_input = input_string.split()
    number = user_input[0]
    initial_unit = user_input[1]
    convert_to_unit = user_input[2]

    return (number, initial_unit, convert_to_unit)


def kilometers_convert(km, unit):
    convertTo = {
            "mm": 1000 * 1000,
            "cm": 100 * 1000,
            "m": 0.001,
            "mi": 1 / 0.621371,
            "ft": 1 / 0.621371 * 5280,
            "in": 1 / 0.621371 * 5280 * 12
            }
    if unit in convertTo:
        value = float(km)
        return value * convertTo[unit]
    else:
        return "Conversion not implemented"


print("Unit converter usage.  25 km m")
print("kilometer conversions supported: mm, cm, m, mi, ft, in")
print("Example:  type: 1 km cm ")
print(" Result:  1 km is 100 cm")

while(True):
    print("> ", end="")
    user_conversion_request = input()
    if (user_conversion_request == "exit"):
        break

    conversion_parts = inputeval(user_conversion_request)
    orig_unit = conversion_parts[1]
    unit_value = conversion_parts[0]
    convert_unit = conversion_parts[2]

    print(unit_value, orig_unit, "is", kilometers_convert(unit_value, convert_unit), str(convert_unit))
