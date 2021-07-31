local_val = "magical unicorns"


def square(x):
    return x * x


class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"


# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())


# print(locals())
print('*'*100)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print(" The file is being executed becaue it is imported by another file. the file is called :" , __name__)
