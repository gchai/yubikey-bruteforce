#mymodule.py
import sys, getopt
import subprocess
import time
import threading

# lockcode = "00000000000000000000000000000000"
# maxlockcode="340282366920938463463374607431768211455"

def func(args):
    return args

def crack_lock(low, high):
    print(f"Cracking with {low} and {high}!")
    for i in range(low, high+1):
        completed = 0
        while completed == 0:
            # HEX-ifies the string
            lockcode = str(hex(i))

            # Removes the 0x
            lockcode = lockcode[2:].zfill(32)

            print(lockcode)

            bashCommand = f"ykman config set-lock-code --clear --force --lock-code {lockcode}"
            process = subprocess.run(bashCommand.split(), capture_output=True, text=True)
            if "WARNING" not in process.stderr:
                completed = 1
            else:
                print(f"TOO FAST, retrying {lockcode}")
            if (("WARNING" not in process.stderr) and ("ERROR" not in process.stderr)):
                print(f"Complete with {lockcode}!")
                f = open(f"{lockcode}.txt", "a")
                f.write(lockcode+"\n"+process)
                f.close()

def main(argv):
    start=0
    end=0
    threads=0

    opts, args = getopt.getopt(argv,"t:s:e:")
    for opt, arg in opts:
        if opt == '-t':
            threads = int(arg)
        elif opt == '-s':
            start = int(arg)
        elif opt == '-e':
            end = int(arg)

    difference = end - start
    
    if difference%threads != 0:
        print("The difference must be divisable by threads! Exiting!")
        sys.exit()
    slices = difference//threads-1



    for i in range(threads):
        
        if i == threads-1:
            end = start+slices+1
        else:
            end = start+slices


        t = threading.Thread(target=crack_lock, args=(start,end))
        t.start()
        start = end+1

 
    print("Done!")

if __name__ == "__main__":
    main(sys.argv[1:])