def generate_snowflake(crystals):
    lines = crystals.split("\n")
    return_lines = []
    for i in range(len(lines)):
        return_lines.append(lines[i]+lines[i][::-1])

    return "\n".join(return_lines)

if __name__ == '__main__':
    print(generate_snowflake("* \n *\n* "))
    print(generate_snowflake("X=~"))
    print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
    print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
    print(generate_snowflake("*  -\n * -\n*  -"))
