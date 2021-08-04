#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (u,l))

up_low("Hello Mr. Pender, how are you this Tuesday afternoon?")
