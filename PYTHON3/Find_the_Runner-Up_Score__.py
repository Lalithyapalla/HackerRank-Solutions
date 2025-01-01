if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   # print(sorted(set(arr))[-2])
    ss=set(arr)
    s=sorted(ss)
    print(s[-2])
