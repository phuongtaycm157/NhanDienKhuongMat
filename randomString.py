import random, string


def randomString(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
