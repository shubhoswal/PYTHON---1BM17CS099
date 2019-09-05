import string
import random
i=1
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size=random.randint(8,12)
    return ''.join(random.choice(chars) for x in range(size))
while i!=-1:
    print(randompassword())
    print('Enter 1 to generate password and -1 to exit')
    i=int(input())
