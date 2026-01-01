def decode(s):
    while '(' in s and ')' in s:
        first_invoke = s.rfind('(')    # Find the innermost opening parenthesis
        last_invoke = s.find(')', first_invoke)  # Find the corresponding closing parenthesis
        # Reverse the substring inside the parentheses
        s = s[:first_invoke] + s[first_invoke+1:last_invoke][::-1] + s[last_invoke+1:]
    return s

if __name__ == "__main__":
    decode("((is?)(a(t d)h)e(n y( uo)r)aC)")
    decode("(f(b(dc)e)a)")
    decode("f(Ce(re))o((e(aC)m)d)p")