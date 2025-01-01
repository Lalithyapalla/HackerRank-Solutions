def print_rangoli(size):
 alphabet=[chr(i) for i in range(97,123)]
 alphabet=alphabet[:size]
 indices=list(range(size))
 indices=indices[0:-1]+indices[::-1]
 for i in indices:
     ind=i+1
     org=alphabet[-ind:]
     rev=org[::-1]
     row=rev+org[1:]
     width=size*4-3
     row='-'.join(row)
     print(row.center(width,'-'))
  

