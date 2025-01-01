

# Complete the solve function below.
def solve(s):
    result = ''
    for i in range(0, len(s)):
        if i == 0:
            result = result + s[i].upper()
        elif s[i] != ' ' and s[i-1] == ' ':
            cap = s[i].upper()
            result = result + cap
        else:
            result = result + s[i]
    return result

