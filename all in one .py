list1=[1,2,3,4,5,6,7,8,9,10]
dobule_number=[num*2 for num in list1]
print(dobule_number)
def square(n):
    return n*n
list1=[1,2,34,44,6,6,6,7,8,99,12]
result=map(square,list1)
print(list(result))
name=["rehan","zohan","rania"]
rollno=[100,200,300]
mapped=zip(name,rollno)
print(list(mapped))
ages=[19,45,12,78]
for age in ages:
    if age < 18:
        print(age, "not allowed")
        print(exit)
        exit()
    else:
       print(age,"allowed")