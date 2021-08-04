#Write a python function to reverse a string, then ask the users for a string to test it.

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Greek Yoghurt"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))
