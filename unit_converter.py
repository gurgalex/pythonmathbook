
def inputeval(input_string):
    user_input = input_string.split()
    number = user_input[0]
    initial_unit = user_input[1]
    convert_to_unit = user_input[2]

    return (number, initial_unit, convert_to_unit)


def metersTo(meter, unit):
    m = 1
    convertTo = {
            "mm": m * 1000,
            "cm": m * 100,
            "m": m,
            "in": m * 100 / 2.51,
            "km": m / 1000,
            "mi": m * 0.621371 / 1000,
            "ft": m * 0.623171 / 1000 * 5280,
            }

    if unit in convertTo:
        value = float(meter)
        return value * convertTo[unit]
    else:
        return "Invalid unit conversion"


def kiloMetersTo(km, unit):
    convertTo = {
            "mm": 1000 * 1000,
            "cm": 1000 * 100,
            "m": 1000,
            "mi": 0.621371,
            "ft": 0.621371 * 5280,
            "in": 0.621371 * 5280 * 12
            }

    if unit in convertTo:
        value = float(km)
        return value * convertTo[unit]
    else:
        return "Conversion not implemented"


print("Unit converter usage.  25 km m")
print("Original units supported:  km, m")
print("Conversions to supported: mm, cm, m, mi, ft, in")
print("Example: type: 1 km cm")
print("Result:  1 m is 100 cm")

conversionSelector = { #original units supported
        "m": metersTo,  # "m" calls the metersTo function_base
        "km": kiloMetersTo
        }

while(True):
    print("> ", end="")
    user_conversion_request = input()
    if (user_conversion_request == "exit"):
        break

    conversion_parts = inputeval(user_conversion_request)
    orig_unit = conversion_parts[1]
    unit_value = conversion_parts[0]
    convert_unit = conversion_parts[2]

    # orig unit is the key and is replaced with the function to call.
    # Then the paramters are supplied to that function
    print(unit_value, orig_unit, "is",
          conversionSelector[orig_unit](unit_value, convert_unit),
          str(convert_unit))
