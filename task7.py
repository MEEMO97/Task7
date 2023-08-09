# 1st Question
def num_loop(num):
    for i in range(1, num+1):
        for x in range(1,i+1):
            print(x,end=" ")
        print()
# 2nd Question
def sum_num(num):
    summ =0
    for i in range(1,num+1):
        summ+=i
    print(summ)
# 3rd Question
def name_loop(name):
    for i in range(0, len(name)):
        for x in range(0, i+1):
            print(name[x],end=" ")
        print()
    for i in reversed(range(0, len(name))):
        for x in range(0, i):
            print(name[x], end=" ")
        print()
# 4th Question
def name_reversed(name):
    for i in reversed(range(0, len(name))):
        print(name[i],end="")
# 5th Question
def num_desc(num):
    while num >=1:
        print(num,end=" ")
        num-=1
# 6th Question
def multiply_five():
    for i in range(1,11):
        print(5*i,end=" ")
# 7th Question
def multiply(limit,target,max):
    for i in range(1,max+1):
        if target*i>limit:
            print("this is your limit")
            break
        else:print(target*i,end=" ")

