def compute_score(judge_scores, *penalties):

    max_score = max(judge_scores)
    min_score = min(judge_scores)

    judge_scores.remove(max_score)
    judge_scores.remove(min_score)

    judge_scores = sum(judge_scores)

    for penalty in penalties:
        judge_scores -= penalty

    return judge_scores
