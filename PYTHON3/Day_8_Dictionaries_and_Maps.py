# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phone_book={}
for _ in range(n):
    detail=input().split()
    name=detail[0]
    num=detail[1]
    phone_book[name]=int(num)
    
while True:
    find_name=input()
    if find_name in phone_book:
        print(f'{find_name}={phone_book[find_name]}')
    else:
        print('Not found')
