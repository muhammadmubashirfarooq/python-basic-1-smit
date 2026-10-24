#print('Hello world')
#   ==========lists topic============

fruits=['mango','banana','watermelon']
print(fruits)

# print(fruits.append('cherry'))

fruits[1]="cherry"
print(fruits)
fruits.insert(2,"grapes")
print(fruits)
fruits.pop(1)
print(fruits)

#==========extend========
fruits_2 = ["peach","orange"]
fruits.extend(fruits_2)
print(fruits)

#==========sort==========
fruits.sort()
fruits_rev=fruits.sort(reverse=True)
print(fruits_rev)
