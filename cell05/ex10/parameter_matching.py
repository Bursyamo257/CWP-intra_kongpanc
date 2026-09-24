#!/usr/bin/env python3
import sys
def main() :
    hello = input("What was the parameter? ")
    if sys.argv[1] == hello :
        print("Good job!")
    else :
        print("Nope, sorry...")
main()