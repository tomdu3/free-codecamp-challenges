def number_of_videos(video_size, video_unit, drive_size, drive_unit):

     # Define conversion factors
    UNITS = {
        'B': 1,
        'KB': 1000,
        'MB': 1000000,
        'GB': 1000000000,
        'TB': 1000000000000
    }
    if video_unit not in ['B', 'KB', 'MB', 'GB']:
        return 'Invalid video unit'
    if drive_unit not in ['GB', 'TB']:
        return 'Invalid drive unit'

    return (drive_size * UNITS[drive_unit])//(video_size * UNITS[video_unit])