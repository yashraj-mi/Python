nums = [1,1,1,2,2,3]

dic = {}
k=2
ans=[]
for num in nums:
    if dic.get(num):
        dic[num] += 1
    else:
        dic[num] = 1

sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for key,value in sorted_dic:
    ans.append(key)
print(ans[:k])