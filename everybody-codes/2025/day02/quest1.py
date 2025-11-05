import sys
import json

result = [0, 0]


def calculations(arr: list, cycles: int = 3) -> list:
    global result
    x2, y2 = arr
    for i in range(cycles):
        [x1, y1] = result
        [x1, y1] = [x1 * x1 - y1 * y1, x1 * y1 + x1 * y1]
        [x1, y1] = [x1 // 10, y1 // 10]
        [x1, y1] = [x1 + x2, y1 + y2]
        result = [x1, y1]
        print(result)
    return result


input_str = sys.argv[1]
arr = json.loads(input_str[input_str.index("["):])

print(str(calculations(arr)).replace(" ", ""))
