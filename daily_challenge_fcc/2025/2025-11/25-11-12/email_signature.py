def generate_signature(name, title, company):
    """
    Generate an email signature based on the first letter of the name.
    The signature format is:
    - Names starting with A-I: ">>Name, Title at Company"
    - Names starting with J-R: "--Name, Title at Company"
    - Names starting with S-Z: "::Name, Title at Company"
    Parameters:
    name (str): The person's name.
    title (str): The person's job title.
    company (str): The person's company.

    Returns:
    str: The formatted email signature.

    Example:
    >>> generate_signature("Quinn Waverly", "Founder and CEO", "TechCo")
    '--Quinn Waverly, Founder and CEO at TechCo'
    """

    if name[0].upper() >= 'A' and name[0].upper() <= 'I':
        prefix = '>>'
    elif name[0].upper() >= 'J' and name[0].upper() <= 'R':
        prefix = '--'
    else:
        prefix = '::'
    return f"{prefix}{name}, {title} at {company}"