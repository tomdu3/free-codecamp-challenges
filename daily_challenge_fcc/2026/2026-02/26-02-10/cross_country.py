def get_relative_results(times):
    # Convert "H:MM:SS" to total seconds
    total_seconds = []
    for t in times:
        h, m, s = map(int, t.split(':'))
        total_seconds.append(h * 3600 + m * 60 + s)
        
    # The winner's time (fastest)
    winner_time = total_seconds[0]
    
    # Calculate differences and format
    results = []
    for t in total_seconds:
        diff = t - winner_time
        if diff == 0:
            results.append("0")
        else:
            mins = diff // 60
            secs = diff % 60
            results.append(f"+{mins}:{secs:02d}")
    return results
