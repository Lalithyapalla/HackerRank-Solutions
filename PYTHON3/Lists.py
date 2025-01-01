if __name__ == '__main__':
    n = int(input())
    list=[]
    for _ in range(n):
        command_line=input().split()
        command=command_line[0]
        if command=="insert":
            i,e=map(int,command_line[1:])
            list.insert(i,e)
        elif command=="print":
            print(list)
        elif command=="remove":
            e=int(command_line[1])
            list.remove(e)
        elif command=="append":
            e=int(command_line[1])
            list.append(e)
        elif command=="sort":
            list.sort()
        elif command=="pop":
            list.pop()
        elif command=="reverse":
            list.reverse()
        
        
            
