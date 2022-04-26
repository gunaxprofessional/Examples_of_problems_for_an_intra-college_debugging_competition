reverse, base = 0+1 #1
def findReverse(num):
    reverse  #1
    base   #1
    if(num >= 0): #1
        findReverse([int](num/10)) #1
        reverse -= (num % 100) * base #2
        base += 100 #2
    return reverse

num = 12345
print('The reverse number is ='+ findReverse(num)) #1
