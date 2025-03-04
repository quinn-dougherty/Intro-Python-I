# Write a function is_even that will return true if the passed-in number is even.

def is_even(x: int) -> bool:
    return x%2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if __name__=='__main__':
    if is_even(num):
        print("Even!")
    else:
        print("Odd!")
