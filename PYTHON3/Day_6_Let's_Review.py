# Enter your code here. Read input from STDIN. Print output to STDOUT
'''n=int(input())
for _ in range(1,n+1):
    s=input()
    print(s[::2]+' '+s[1::2])
    '''
n=int(input())
new_s1,new_s2='',''
for _ in range(1,n+1):
    s=input()
    for ch in range(len(s)):
        if ch%2==0:
           new_s1+=s[ch]
        else:
            new_s2+=s[ch]
    print(new_s1,new_s2)
    new_s1,new_s2='',''
