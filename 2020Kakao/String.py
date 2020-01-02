s = "ababcdcdababcdcd"

max_window_size = len(s) // 2
min_val = len(s)

for c in range(1, max_window_size + 1):
    result = len(s)
    i = 0
    while i < len(s) - 1:
        tmp = s[i : i + c]
        j = i + c
        cnt = 0
        while j <= len(s) - c and tmp == s[j : j + c]:
            cnt += 1
            if cnt >= 2:
                result -= c
            else:
                result -= c - 1
            j += c
        i = j
    if result < min_val:
        min_val = result

print(min_val)
