numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def even(num):
  
	if num % 2 != 0:
   
 	 return False
  
	else:
      
 	 return True


print "even(1):\t\t\t\t", even(1)

print "even(2):\t\t\t\t", even(2)

print "*"*50



def odd(num):

    if num % 2 != 0:

        return True

    else:

        return False


print "even(1):\t\t\t\t", odd(1)

print "even(2):\t\t\t\t", odd(2)

print "*"*50



def count_odd(list):

    count = 0

    for i in range(len(list)):

        if list[i] % 2 != 0:

            count = count + 1

    return count


print "count_odd([1, 2, 3, 4, 5, 6, 7, 8]):\t", count_odd(numbers)

print "*"*50



def reverse(list):

    list.reverse()

    return list

print "reverse([1, 2, 3, 4, 5, 6, 7, 8]):\t", reverse(numbers)

print "*"*50



def merge(list1, list2):

    newList = []

    while(list1 and list2):

        if(list1[0] <= list2[0]):

            temp = list1.pop(0)

            newList.append(temp)

        else:

            temp = list2.pop(0)

            newList.append(temp)

    newList.extend(list1 + list2)

    return newList

print "merge([1, 3, 5, 7], [2, 4, 6, 8]):\t", merge([1, 3, 5, 7], [2, 4, 6, 8]) 
print"*"*50


