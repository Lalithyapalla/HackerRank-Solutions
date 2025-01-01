def count_substring(string, sub_string):
    count=0
    while string.find(sub_string)!=-1:
        if string.find(sub_string)!=-1:
            string=string[string.find(sub_string)+1:]
            count+=1
    return count

