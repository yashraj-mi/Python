def canJump( nums):
        maxreach=0
        for i  in range(len(nums)):
            if i<=maxreach:
                maxreach=max(maxreach, i+nums[i])
        return maxreach>=len(nums)-1
    
    
    
    
    
    
    
    
def canJump2(nums):
        jump=0
        maxreach=0
        for i  in range(len(nums)):
            if i<=maxreach:
                maxreach=max(maxreach, i+nums[i])
                jump+=1
            if maxreach>=len(nums)-1:
                return jump
        
print(canJump2([2,3,1,1,4]))