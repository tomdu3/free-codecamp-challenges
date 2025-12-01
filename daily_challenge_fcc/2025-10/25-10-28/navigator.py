def navigate(commands: list) -> str:
    navigations = []
    forward = None 
    for command in commands:
        if 'visit' in command.lower():
            position = command.split(' ', 1)[1]
            navigations.append(position)
            forward = None
        elif 'back' in command.lower():
            if navigations:
                forward = navigations.pop()
        elif 'forward' in command.lower():
            if forward:
                navigations.append(forward)
                forward = None
    position = navigations[-1] if navigations else "Home"


    return position