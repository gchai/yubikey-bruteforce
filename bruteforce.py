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
                print("TOO FAST")
            if (("WARNING" not in process.stderr) and ("ERROR" not in process.stderr)):
                print(f"Complete with {lockcode}!")
                f = open(f"{lockcode}.txt", "a")
                f.write(lockcode+"\n"+process)
                f.close()
 
 
if __name__ =="__main__":
    t1 = threading.Thread(target=crack_lock, args=(5000,10000))
    t2 = threading.Thread(target=crack_lock, args=(10000,15000))
    t3 = threading.Thread(target=crack_lock, args=(15000,20000))
    t4 = threading.Thread(target=crack_lock, args=(20000,25000))
    t5 = threading.Thread(target=crack_lock, args=(25000,30000))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
 
    print("Done!")