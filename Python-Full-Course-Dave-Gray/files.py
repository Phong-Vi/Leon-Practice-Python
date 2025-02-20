# r = read
# a = append
# w = write
# x = create

# Read - error if it doesn't exist
f = open("names.txt", "r")
# print(f.read())   # read whole file
# print(f.read(4))    # read 4 characters

# print(f.readline())   # read line by line
# print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("more_names.txt")
#     print(f.read())
# except:
#     print("The file you want to read does not exist")
# finally:
#     f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil\r\n")
f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read does not exist")
finally:
    f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

# Two ways to create a new file
# Opens a file for writing, creates the file if it does not exist
# f = open("more_list.txt", "w")
# f.close()

# Creates the specified file, but returns an error if the file exists
import os

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()


# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete doesn't exist")

# **** Good way to work with file: use with ****
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)