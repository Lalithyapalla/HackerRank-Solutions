def minion_game(string):
    vowels='AEIOU'
    kevin=stuart=0
    length=len(string)
    for i in range(length):
        if string[i]in vowels:
            kevin+=length-i
        else:
            stuart+=length-i
    if stuart>kevin:
        print(f'Stuart {stuart}')
    elif kevin>stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

