# class JustNotCoolError(Exception):
#     pass

# x = 2
# try:
#     # print(x/0)
#     # if not type(x) is str:
#     #     raise TypeError('Only strings are allowed.')
#     raise JustNotCoolError('This just is not cool, man.')
# except NameError:
#     print('NameError means something is probably undefined.')
# except ZeroDivisionError:
#     print('Please do not devide by zero.')
# except Exception as error:
#     print(error)
# else:
#     print('No errors!')
# finally:
#     print('I am going to print with or without an error.')

########################################################################
# Here is an example of defining and using a custom exception in Python:

# Define a custom exception
class JustNotCoolError(Exception):
    def __init__(self, message="This is just not cool!"):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def check_coolness(is_cool):
    if not is_cool:
        raise JustNotCoolError("You are not cool enough!")

# Example usage
try:
    check_coolness(False)
except JustNotCoolError as e:
    print(e)  # Output: You are not cool enough!
else:
    print('You are cool 👍!')