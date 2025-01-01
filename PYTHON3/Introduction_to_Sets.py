def average(array):
    Set=set(array)
    total=sum(Set)
    avg=float(total/len(Set))
    r=round(avg,3)
    return r

