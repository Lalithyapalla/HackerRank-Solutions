def increasing(i):
    return '.|.'*(2*i+1)
def decreasing(i,n):
    return '.|.'*(2*(n-i-1)+1)
def create(n,M):
    for i in range(n):
        if i<n//2:
            pattern=increasing(i)
        elif i==n//2:
            pattern='WELCOME'
        else:
            pattern=decreasing(i,n)
        print(pattern.center(M,'-'))

if __name__ == '__main__':
    n, M = map(int, input().split())
    create(n, M)
