# learningPython
new to Python
#hailstorm
x=20
while x >1:
    if x %2 == 0:
        x //=2
    else:
        x = 3*x+1
    print(x)

#count hailstorm

x=14
count=0
while x >1:
    count +=1
    if x %2 == 0:
        x //=2
    else:
        x = 3*x+1
print(count)

#compard time 
import datetime
start = datetime.datetime.now()
end = datetime.datetime.now()
print(end-start)


#count 1-1000 hialstorm count numbers

for i in range (1,100001):
    count=0
    x = i
    while x >1:
        count +=1
        if x %2 == 0:
            x //=2
        else:
            x = 3*x+1
    print(i, count)

#orginal model 
    #if print(count), time=0:00:21.657643
    #if not, time =0:00:02.738720
import datetime
start = datetime.datetime.now()
for i in range (1,1000001):
    count=0
    x = i
    while x >1:
        count +=1
        if x %2 == 0:
            x //=2
        else:
            x = 3*x+1
end = datetime.datetime.now()
print(end-start)



#update 1 == append
#time == 0:00:23.363213
import datetime
start = datetime.datetime.now()
result = ['NA']
for i in range (1,10000001):
    count=0
    x = i
    while x >1:        
        count +=1
        if x %2 == 0:
            x //=2
        else:
            x = 3*x+1

        if i > x :
             count += result[x]
             break #not sure why break is so important here
    result.append(count)
end = datetime.datetime.now()
print(end-start)

#broken down into some similar subproblems。
#every subproblem only needs to be solved just one time
#sotre all the sulotions to all subproblems

# update 2 dictionary
#time==0:00:31.915281
import datetime
start = datetime.datetime.now()
result = {1:1}
for i in range (1,10000001):
    count=0
    x = i
    while x not in result:
        count +=1
        if x %2 == 0:
            x //=2
        else:
            x = 3*x+1
        if i > x :
            count += result[x]
            break
    result.update({i:count})
result
end = datetime.datetime.now()
print(end-start)

# complicated dynamic programming  1
#time = 0:00:23.782090
import datetime
start = datetime.datetime.now()

result = {1:0}
for i in range (1,10): 
    x = i
    lst=[]
    count = 0
    while x not in result:
        lst.append(x)
        count += 1
        if x %2 == 0:
            x //=2
        else:
            x = 3*x+1
    count = count + result[x]
    for j in lst:
        result[j] = count
        count -= 1
result
end = datetime.datetime.now()
print(end-start)



### COMPLICATED DYNAMIC PROGRAMMING  2
#time = 0:00:22.228003
import datetime
st = datetime.datetime.now()

outp = {1:0}
for x_init in range(1,10000001):
    x = x_init
    lst = []
    while x not in outp:
        lst.append(x)
        if x%2==0:
            x //= 2
        else:
            x = 3*x + 1
    lst.reverse()
    count = outp[x]+1
    for item in lst:
        outp[item] = count
        count += 1
        
nd = datetime.datetime.now()

print(nd-st)




#Pascal Triangle
a =[1]
print(a)
for i in range(10):
    b=[1]
    for j in range(len(a)-1):
        b.append(a[j]+a[j+1])
    b.append(1)
    print(b)
    a = b
