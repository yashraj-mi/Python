intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
ans=[intervals[0]]
for i  in  range(1,len(intervals)):
    curr=intervals[i]
    last=ans[-1]
    if  curr[0]<=last[1]:
        last[1]=max(last[1],curr[1])
    else:
        ans.append(curr)
   
print(ans)