from datetime import datetime, timedelta

def digital_detox(logs):
    # Convert all logs to datetime objects
    dt_logs = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    
    # Sort logs by time
    dt_logs.sort()
    
    # Check condition 1: No more than once within any four-hour period
    for i in range(len(dt_logs)):
        for j in range(i + 1, len(dt_logs)):
            if dt_logs[j] - dt_logs[i] <= timedelta(hours=4):
                return False
    
    # Check condition 2: No more than 2 times on any single day
    daily_counts = {}
    for log in dt_logs:
        date_str = log.strftime("%Y-%m-%d")
        daily_counts[date_str] = daily_counts.get(date_str, 0) + 1
        if daily_counts[date_str] > 2:
            return False
    
    return True

if __name__ == "__main__":
    print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
    print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
    print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
    print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
    print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
    print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
    