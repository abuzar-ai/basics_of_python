#two types of loops existing "while & For"

#while loops
#while loops are used to execute a block of code multiple times
x=0
# # while x!=100:
#     print(x)
#     x=x+1

#For loops
# for x in range(2,37):
#     print(x)

# applications
days=("mon,tues, wed,thur,friday,sat,sun")
for d in days:   
    if (d=="friday"):break   #loops stops whn run this line on friday
    if(d=="friday"):continue #skips friday and continue others
    print(d)
