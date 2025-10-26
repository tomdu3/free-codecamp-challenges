import datetime as dt

def format(seconds):
    """Formats a duration given in seconds into a human-readable string.
    Args:
        seconds (int): Duration in seconds.
    Returns:
        str: Formatted duration string.
    """    
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    secs = remaining_seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"