from typing import Any
from collections import Counter
def most_frequent(data: list) -> Any:
    counter = Counter(data)
    return counter.most_common(1)[0][0]
    