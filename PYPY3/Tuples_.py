if __name__ == '__main__':
    n = int(input())
    #integer_list = map(int, input().split())
    N=input().split()
    t=tuple(map(int,N))
    print(hash(t))
