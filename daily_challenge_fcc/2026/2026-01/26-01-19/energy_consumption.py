def compare_energy(calories_burned, watt_hours_used):
    workout_energy = calories_burned * 4184
    devices_energy = watt_hours_used * 3600
    if workout_energy > devices_energy:
        return "Workout"
    elif devices_energy > workout_energy:
        return "Devices"
    return "Equal"
