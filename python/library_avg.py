import statistics
# statatics library
print(statistics.mean([100,99]))

#command line argument
#sys - system

import sys

try:
    print("hello , my name is",sys.argv[1])
except IndexError:
    print("too few arguments")