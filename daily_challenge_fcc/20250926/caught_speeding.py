def speeding(speeds, limit):
    speeds = [speed - limit for speed in speeds if speed > limit]

    return [len(speeds), sum(speeds)/len(speeds)] if len(speeds) != 0 else [0, 0]