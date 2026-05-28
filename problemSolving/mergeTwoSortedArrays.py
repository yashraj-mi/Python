nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m=len(nums2)
n=len(nums1)-m

i=0
j=0
ans=[]

while(i<n and j<m):
    
    
    if nums1[i]<=nums2[j]:
        ans.append(nums1[i])
        i+=1
    else:
        ans.append(nums2[j])
        j+=1
    
    

if i==n:
    ans.extend(nums2[j:])
else:
    ans.extend(nums1[i:])
    
    
print(ans)