#write a program to reverse a string
def reverse_string(s):
    print("The original string:",s)
    s=s[::-1]
    return s

s=input("Enter the string")
print("The reversed string:",reverse_string(s))