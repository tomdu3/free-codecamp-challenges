def adjust_thermostat(temp, target):
    output_arr = ['heat', 'cool', 'hold']
    if temp != target:
        # If temp > target, index is 1 ('cool'); if temp < target, index is 0 ('heat')
        return output_arr[int(temp > target)]
    # If temp == target, hold the current setting
    return output_arr[2]
