#!/usr/bin/env python

import os, sys, time

def main():  
    print ("AutoRes is starting")
    executable = sys.executable
    print ("executing is ..",executable)

    args = sys.argv[:]
    args.insert(0, sys.executable)
    time.sleep(2)
    print ("Respawning")
    os.execvp(executable, args)

if __name__ == "__main__":  
    main()
