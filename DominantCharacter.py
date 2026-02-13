#CodeForce

""" 
1. The length of the substring is at least 2.
2. 'a' occurs strictly more times in this substring than 'b'.
3. 'a' occurs strictly more times in this substring than 'c'.

To solve this problem efficiently, we can use a sliding window approach. We will iterate through the string and maintain a window of characters. For each window, we will count the occurrences of 'a', 'b', and 'c'. If the window satisfies the conditions, we will update the minimum length. We will continue this process until we find the smallest valid substring or determine that no such substring exists.
 """
from ast import In


def smallest_dominant_substring(s):
    n = len(s)
    min_length = float('inf')
    
    for i in range(n):
        count_a = count_b = count_c = 0
        for j in range(i, n):
            if s[j] == 'a':
                count_a += 1
            elif s[j] == 'b':
                count_b += 1
            elif s[j] == 'c':
                count_c += 1
            
            if j - i + 1 >= 2 and count_a > count_b and count_a > count_c:
                min_length = min(min_length, j - i + 1)
                break
    
    return min_length if min_length != float('inf') else -1

# Example usage
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(smallest_dominant_substring(s))
""" ```In this code:
- We define a function `smallest_dominant_substring` that takes a string `s` as input and returns the length of the smallest valid substring or -1 if no such substring exists.
- We use two nested loops to create a sliding window. The outer loop starts from the beginning of the string, and the inner loop extends the window until we find a valid substring or reach the end of the string.
- We maintain counts of 'a', 'b', and 'c' within the current window. If the window satisfies the conditions, we update the minimum length and break out of the inner loop to check the next starting point.
- Finally, we return the minimum length found or -1 if no valid substring exists. """