def merge_the_tools(string, k):
    start=0
    end=k
    while end<=len(string):
        temp=string[start:end]
        chunk=list(set(list(temp)))
        print(''.join(chunk))
        start+=k
        end+=k
     

