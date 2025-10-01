def number_of_files(file_size, file_unit, drive_size_gb):
    """Calculate the number of files that can fit on a drive."""
    
    # Define conversion factors
    UNITS = {
        'B': 1,
        'KB': 1000,
        'MB': 1000000,
        'GB': 1000000000,
    }

    # Calculate drive size in bytes and return the number of files that fit
    return (drive_size_gb * UNITS['GB'])//(file_size*UNITS[file_unit])