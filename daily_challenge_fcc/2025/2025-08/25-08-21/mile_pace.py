def mile_pace(miles, duration):
    duration_parts = duration.split(":")
    total_seconds = int(duration_parts[0]) * 60 + int(duration_parts[1])
    pace_seconds = total_seconds / miles
    pace_minutes = int(pace_seconds // 60)
    pace_seconds_remainder = int(pace_seconds % 60)
    return f"{str(pace_minutes).zfill(2)}:{str(pace_seconds_remainder).zfill(2)}"
