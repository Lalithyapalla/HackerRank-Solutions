if __name__ == '__main__':
    d={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in d:
            d[score]=[name]
        else:
            d[score].append(name)
    s=sorted(d.items())[1][1]
    if len(s)==1:
     print('\n'.join(s))
    else:
        print('\n'.join(s[::-1]))
