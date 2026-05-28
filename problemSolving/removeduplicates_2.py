nums=[0,0,0,0,1,1,1,1,1,2,3,3]

if len(nums)<=2:
    nums

ans=nums[:2]


for i  in range(2,len(nums)):
    if nums[i]==nums[i-2]:
        continue
    ans.append(nums[i])
    
    
print(ans)
