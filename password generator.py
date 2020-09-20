
print('hey there, lets make an awesome password together!')

import string, random
def generatePassword(num):
    password = ''
    
    for n in range(num):
        x = random.randint(0,60)
        password += string.printable[x]
        
    return password
print (generatePassword(16))



    
    