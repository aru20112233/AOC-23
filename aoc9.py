# from math import comb

# with open("day9.txt", "r") as file:
#     lines = file.readlines()
#     total_sum = 0

#     for line in lines:
#         formatted_line = line.split()
#         # print(len(formatted_line))
#         for index, value in enumerate(formatted_line):
#             pascal = comb(len(formatted_line), index)
#             total_sum += int(value) * pascal * (-1) ** (len(formatted_line) - index + 1)

#     print(f"total: {total_sum}")

history=open('day9.txt').readlines()

from math import comb
def Lagrange1(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i)*(-1)**(n-1-i)
    return res

def Lagrange2(nums):
    n=len(nums)
    res=0
    for i,x in enumerate(nums):
        res+=x*comb(n,i+1)*(-1)**(i)
    return res

res1,res2=0,0
for line in history:
    nums=list(map(int,line.strip().split()))
    res1+=Lagrange1(nums)
    res2+=Lagrange2(nums)
print(res1,res2,sep=' ')

