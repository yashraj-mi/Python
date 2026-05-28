for i in range(5):
    space=' '*(5-i-1)
    star='*'*(2*i+1)
    
    print(f"{space}{star}")
    
    
    
    
    # *************************************************
    
    
    
for i in range(5):
    space=' '*(5-i-1)
    nums=[]
    for  j in range(1,i+2):
        nums.append(j)
        
    for k in range(1,i+1):
        nums.append(i+1-k)
        
        
    temp="".join(map(str,nums))
    
    print(f"{space}{temp}")
    
    
# ***************************************************






