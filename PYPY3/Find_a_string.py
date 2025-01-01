def count_substring(string, sub_string):
    c=0
    ind=0
    for i in range(len(string)):
        if string.find(sub_string,ind)!=-1:
            c+=1
            ind=string.find(sub_string,ind)+1
        else:
            break
    return c

