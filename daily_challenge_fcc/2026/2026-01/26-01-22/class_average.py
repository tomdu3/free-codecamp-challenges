def get_average_grade(scores):

    score_range = {
         (97,100): "A+",
         (93,96): "A",
         (90,92): "A-",
         (87,89): "B+",
         (83,86): "B",
         (80,82): "B-",
         (77,79): "C+",
         (73,76): "C",
         (70,72): "C-",
         (67,69): "D+",
         (63,66): "D",
         (60,62): "D-",
         (0,59 ): "F",
    }

    total_score = sum(scores)
    average_score = total_score // len(scores)

    for range in score_range:
        if range[0] <= average_score <= range[1]:
            return score_range[range]

    return None
