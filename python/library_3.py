import sys
from sayings import goodbye

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello,{name}")
def goodbye(name):
    print(f"goodbye,{name}")

if __name__ == "__main__":
    main()


if len(sys.argv) == 2:
    goodbye(sys.argv[1])