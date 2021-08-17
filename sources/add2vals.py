'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argunumbers == 3:
    print("")
    print("The result is " + str(calc.mul3(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))))
    print("")
    sys.exit(0)
    
elif argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)

elif argnumbers != 3 and argnumbers != 2:
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'add2vals X Y' where X and Y are individual values. or 'mul3vals' XYZ where xyz are individual values.")
    print("       If add2vals is not in your path, usage is './add2vals X Y'.")
    print("       If unbundled, usage is 'python add2vals.py X Y'.")
    print("")
    sys.exit(1)
