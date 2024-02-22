#  O(n*m)

def naive_search(string, pattern):
    M = len(pattern)
    N = len(string)

    for i in range(N - M + 1):
        j = 0
        while j < M:
            if string[i + j] != pattern[j]:
                break
            j+=1
            
        if j == M:
            return i
    return -1

main_str = "ABABDABAKARICDABABCABAB"
pattern = "KARI"
pos = naive_search(main_str, pattern)
print(pos)