def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:   
        try:
            x = int(input("what is x "))
           # print(f"x is {x}")# f is format string
        except ValueError:
            print("x is not integer")
            # pass
            pass 
        else:
            break
    return x
main()