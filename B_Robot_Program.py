t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    current_position = x 
    first_hit = -1
    
    for i in range(n):
        if s[i] == 'L':
            current_position -= 1
        else:
            current_position += 1
        
        if current_position == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    answer = 1
    remaining = k - first_hit
    
    current_position = 0
    cycle_length = -1
    
    for i in range(n):
        if s[i] == 'L':
            current_position -= 1
        else:
            current_position += 1
        
        if current_position == 0:
            cycle_length = i + 1
            break
    
    if cycle_length != -1:
        answer += remaining // cycle_length
    print(answer)