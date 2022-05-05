players, kim, lim = list(map(int, input().split()))
rounds = 0

while players > 1 and kim != lim:
    players -= players//2
    kim -= kim//2
    lim -= lim//2
    rounds += 1

if players == 1 and kim != lim:
    rounds = -1

print(rounds)
