import subprocess
import time
import threading

# lockcode = "00000000000000000000000000000000"
# maxlockcode="340282366920938463463374607431768211455"
 
def crack_lock(low, high):
    for i in range(low, high):
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
 
 
if __name__ =="__main__":
    t1 = threading.Thread(target=crack_lock, args=(30000,40000))
    t2 = threading.Thread(target=crack_lock, args=(40000,50000))
    t3 = threading.Thread(target=crack_lock, args=(50000,60000))
    t4 = threading.Thread(target=crack_lock, args=(60000,70000))
    t5 = threading.Thread(target=crack_lock, args=(70000,80000))
    t6 = threading.Thread(target=crack_lock, args=(80000,90000))
    t7 = threading.Thread(target=crack_lock, args=(90000,100000))
    t8 = threading.Thread(target=crack_lock, args=(100000,110000))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
 
    print("Done!")