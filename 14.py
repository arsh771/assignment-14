#Q1

list1=[1,4,7,12,25]
list2=[i**3 for i in list1]
print(list2)

#Q2
low=int(input())
high=int(input())
list1=[i for i in range(low,high+1) if i>1 if all(i%j!=0 for j in range(2,i))]
print(list1)

#Q3
#LIST COMPREHENSION:->list comprehensions allow the user to create lists with a for loop with minimal lines of code.

#The comprehensions are not limited to lists.
#You can create dictionaries and sets comprehensions as well.

#GENERATOR EXPRESSION:->Generator is an iterable created using a function with a yield statement. 

#The main feature of generator is evaluating the elements on demand.
#When you call a normal function with a return statement the function
#is terminated whenever it encounters a return statement.
#In a function with a yield statement the state of the function is
#“saved” from the last call and can be picked up the next time you
#call a generator function.



#Q4 
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit=list(map(lambda c:((c*9)/5)+32,Celsius))
print(Fahrenheit)

#Q5


list1=[2,4,5,8,12,13,45]
list2=list(map(lambda x:x*x,list1))
print(list2)


#Q6

def prime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True

lst=[1,2,3,4,5,6,7,21,23]
pr=list(filter(prime,lst))
print(pr)

#Q7

from functools import *
lst=[1,2,3,5,7,12]
w=reduce(lambda x,y:x*y ,lst)
print(w)













