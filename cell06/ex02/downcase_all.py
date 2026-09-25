#!/usr/bin/env python3
import sys

def downcase_it():
    if len(sys.argv) == 1:
        print("none")
    else:
        print(" ".join(arg.lower() for arg in sys.argv[1:]))
downcase_it()