
#n=int(input())
#a=list(map(int,input().split()))
#b=list(map(int,input().split()))
n=5
a=[10,30,5,6,24]
b=[10,41,7,8,24]
#10 30 5 6 24
#10 41 7 8 24
max_a=sum(a)
b_temp=b.copy()
b_temp.sort()
b_temp=b_temp[::-1]
ans_b,t=[],0
for i in b_temp:
    t+=i
    ans_b.append(i)
    if t>=max_a:
        break
ans1=len(ans_b)
rec=0
for i in ans_b:
    rec+=a[b.index(i)]
ans2=max_a-rec
print(ans1,ans2)
