import random
import string

length = input("Length of password: ")
print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase) for _ in range(int(length))))
