# 2026 Winter Games Day 5: Cross-Country Skiing

Passed

Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

- Given times are strings in `"H:MM:SS"` format.
- Given times will be in order from fastest to slowest.
- The winners time (fastest time) should correspond to `"0"`.
- Each other time should show the time behind the winner, in the format `"+M:SS"`.

For example, given `["1:25:32", "1:26:10", "1:27:05"]`, return `["0", "+0:38", "+1:33"]`.
