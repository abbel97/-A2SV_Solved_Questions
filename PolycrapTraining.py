#CodeForce

n = int(input())
tasks = list(map(int, input().split()))

tasks.sort()

day = 1 

for difficulty in tasks:
    if difficulty >= day:
        day += 1 
print(day - 1)