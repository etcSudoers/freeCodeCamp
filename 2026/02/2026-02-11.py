def compute_score(judge_scores:list, *penalties):
    total = 0
    sortedScores = sorted(judge_scores)
    removeFirst = sortedScores[1:]
    removeLast = removeFirst[:-1]
    for i in removeLast:
        total = total + i
    print(f"Total:  {total}")
    final = total - sum(penalties)
    print(f"Penalties: {sum(penalties)}")
    print(f"Final score: {final}")
          
    return final

assert compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) == 64
assert compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 80
assert compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1) == 67
assert compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0) == 67.5
assert compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5) == 59