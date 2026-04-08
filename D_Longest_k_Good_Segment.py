from collections import defaultdict

def find_longest_k_good_segment(n, k, a):
    freq = defaultdict(int)
    left = 0
    max_length = 0
    best_left = 1
    best_right = 1

    for right in range(n):
        freq[a[right]] += 1

        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            best_left = left + 1
            best_right = right + 1

    return best_left, best_right
n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = find_longest_k_good_segment(n, k, a)
print(l, r)