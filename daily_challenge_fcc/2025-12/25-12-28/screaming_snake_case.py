def to_screaming_snake_case(variable_name):
    new_variable_name = ""

    variable_name = variable_name.replace("-", "_")

    for index, char in enumerate(variable_name):
        if char.isupper() and index != 0:
            new_variable_name += "_" + char
        else:
            new_variable_name += char

    return new_variable_name.upper()