def email_chain_count(subject):
    """Count the number of times the email has been forwarded or replied to."""
    re_fwd = ['fw:', 'fwd:', 're:']
    count = 0
    subject_lower = subject.lower()
    for marker in re_fwd:
        if marker in subject_lower:
            count += subject_lower.count(marker)

    return count
