#finding if numbers in a list from 0 to n are prime numbers
def prime(n):
    my_list = list()
    for num in range(2, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            my_list.append(num)
        else:
        	return 'Not prime'
    return my_list


print prime (10)






