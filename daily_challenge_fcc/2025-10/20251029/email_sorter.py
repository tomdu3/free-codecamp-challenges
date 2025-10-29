def sort(emails):

    emails.sort(key=lambda email: email.split('@')[0].lower())
    emails.sort(key=lambda email: email.split('@')[1].lower())

    return emails