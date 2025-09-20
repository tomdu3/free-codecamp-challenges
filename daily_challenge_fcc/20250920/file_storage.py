def number_of_files(file_size, file_unit, drive_size_gb):
    UNITS = {
        'B': 1,
        'KB': 1000,
        'MB': 1000000,
        'GB': 1000000000,
    }
    return (drive_size_gb * UNITS['GB'])//(file_size*UNITS[file_unit])