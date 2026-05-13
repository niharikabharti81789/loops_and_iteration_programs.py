# Loops.............
count = 1
while count <= 14 :
 print(count)
 count+=1
print(count)
# .............

i = 1
while i <= 14 :
 print("niharika",i)
 i+=1
print(i)
# .........................
i=1
while i<= 26:
    print(i)
    i += 1    
    
    
print("loop ended")

# .................................

i=24
while i>= 1:
    print(i)
    i -= 1    
    
    
print("loop ended")

# .................
# practice question................

i=1
while i<= 100:
    print(i)
    i += 1    
    
    
print("loop ended")

# practice question................

i=100
while i>= 1:
    print(i)
    i -= 1    
    
print("loop ended")
 
# practice question,.....................
n=int(input("enter the table of :"))
i=1
while i<= 10:
    print(n*i)
    i += 1  
# practice question,.....................

nums = [12,22,44,8,54,32,567,67,43,221,654,65,]
# traverse
idx = 0 
while idx < len(nums):
    print(nums[idx])
    idx +=1

 # practice question,..................... 

nums =(12,22,44,8,54,32,567,67,43,221,654,65,)

x= 43

i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx ", i)
        break


    else:
        print("not found")
    i +=1
# .....................................
i =1
while i<=5:
    print(i) 
    if(i==3):
        break
    i+=1

print("end of the loop")
# ................................
i=0
while i<=8:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

  
# .........................................
veges = ("peas","carrot","raddish","lockey")

for val in veges:
     print(val)
else:
     print("end")
# .............................................
list=(2,3,2,13,5,43,21,43,21,76,54,43,)
x = 21
idx = 0

for el in list:

    if(el==x):
         
         print ("number found at idx",idx)
         
    idx+=1
#  ...................................
print(range(5))
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
seq = range(5)
for i in seq:
     print(i)
# ...........................
for i in range(10): #range stop
     print(i)


for i in range(2,10): #range start and  stop
     print(i)

for i in range(1,101,2): #range start,stop and step
     print(i)

# prabtice question...................
for i in range(101):
     print(i)

#  prabtice question...................

for i in range(100,0,-1):
     print(i)


#  prabtice question...................

n= int(input("enter the number :"))

for i in range(1,11,):
    print(n*i)
 
#  prabtice question...................
n=8
sum = 0

for i in range(1, n+1):
    sum +=i
print("total sum = ", sum)
# .....................................

n=8
sum = 0
i=1
while i <=n:
    sum+=i
    i+=1

print("total sum = ", sum)
#  prabtice question...................

n=3
fact = 1

for i in range(1, n+1):

    fact = fact * i

print("factorial = ", fact)