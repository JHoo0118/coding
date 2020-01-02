p = ")()()()("


def solution(p):
    trans = {"(": 1, ")": -1, 1: "(", -1: ")"}

    def make_u_and_v(s):
        check = trans[s[0]]
        i = 1
        while check != 0 and i < len(s):
            check += trans[s[i]]
            i += 1
        return (s[:i], s[i:])

    def is_correct(s):
        check = 0
        for c in s:
            check += trans[c]
            if check < 0:
                return False
        return True

    def make_correct(u, v):
        ret = f"({recursion(v)})"
        for c in u[1:-1]:
            ret += trans[-trans[c]]
        return ret

    def recursion(s):
        if not s:
            return s
        u, v = make_u_and_v(s)
        if is_correct(u):
            return u + recursion(v)
        return make_correct(u, v)

    return recursion(p)


print(solution(p))
