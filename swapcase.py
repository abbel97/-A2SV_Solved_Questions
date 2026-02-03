#HackerRank

def swap_case(s):
    newString=""
    for string in s:
        if string.islower():
            newString += string.upper()
        else:
            newString += string.lower()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)