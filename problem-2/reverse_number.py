reverse, base = 0, 1
def findReverse(num):
    global reverse  
    global base   
    if(num > 0):
        findReverse((int)(num/10))
        reverse += (num % 10) * base
        base *= 10
    return reverse

num = 12345
print('The reverse number is =', findReverse(num))
