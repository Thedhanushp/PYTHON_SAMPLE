# + - * / %
#x = int(input("what is x "))
#if x % 2 == 0:
 #   print("x is even number")
#else:
#    print("x is odd")
#
def main():
    x= int(input("what is x : "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")
# bool
def is_even(n):
    if n % 2 == 0 :
        return True
    else:
        return False
main()