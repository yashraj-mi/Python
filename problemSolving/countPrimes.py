import math

def countPrimes(n):
        if n<1:
            return 0
        ans=0
        for i in range(2,n):
            isPrime=True
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    isPrime=False
                    break
                
            if isPrime:
                ans+=1
                
                
        return ans
    
    
print(countPrimes(10))                
                