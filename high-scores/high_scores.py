def latest(scores):
    return scores[-1]



def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
     scores.sort()
     a = scores[-3:]
     a.sort(reverse=True)
     return a