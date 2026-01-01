def decode(s):
    # Base case: if no parentheses, return the string as is
    if '(' not in s or ')' not in s:
        return s
    
    # Find the innermost parentheses
    first_invoke = s.rfind('(')   # innermost opening
    last_invoke = s.find(')', first_invoke)  # corresponding closing
    
    # Reverse the substring inside the parentheses
    inside = s[first_invoke+1:last_invoke]
    reversed_inside = inside[::-1]
    
    # Reconstruct the string without the parentheses
    new_s = s[:first_invoke] + reversed_inside + s[last_invoke+1:]
    
    # Recursively process the new string
    return decode(new_s)

if __name__ == "__main__":
    print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
    print(decode("(f(b(dc)e)a)"))
    print(decode("f(Ce(re))o((e(aC)m)d)p"))
