import re

def validate(email):
    email = email.strip()

    # Check for exactly one '@'
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    # --- Validate local part ---
    # Allowed: letters, digits, dots, underscores, hyphens
    # Cannot start or end with dot
    # Cannot have consecutive dots
    if not re.match(r'^[a-zA-Z0-9._-]+$', local):
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False

    # --- Validate domain part ---
    # Must contain at least one dot
    if '.' not in domain:
        return False

    # Cannot have two dots in a row
    if '..' in domain:
        return False

    # Cannot start or end with dot or hyphen
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False

    # TLD validation: last part after final dot
    tld_match = re.search(r'\.([a-zA-Z]{2,})$', domain)
    if not tld_match:
        return False
    tld = tld_match.group(1)

    # TLD must be at least 2 letters
    if len(tld) < 2:
        return False

    # TLD should contain only letters
    if not re.match(r'^[a-zA-Z]+$', tld):
        return False

    # Allowed characters in domain (excluding dots and hyphens)
    if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_=+{}|;:\'",<>/?`~]+$', domain.replace('.', '').replace('-', '')):
        return False

    # Additional checks: no spaces
    if ' ' in email:
        return False

    return True