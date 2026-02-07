def get_landing_stance(start_stance, rotation):
    # Normalize rotation within 0-360 degrees
    rotation = abs(rotation) % 360
    
    # Since rotations are in multiples of 90, total flip occurs every 180 degrees
    # Determine if rotation is at least 180 degrees
    flip = (rotation // 180) % 2  # 0 or 1
    
    # Decide stance based on flip
    if flip == 0:
        return start_stance
    else:
        # Flip stance
        return "Goofy" if start_stance == "Regular" else "Regular"
