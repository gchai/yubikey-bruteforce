I bought a Yubikey 5C Nano on ebay and it turns out to be an Amazon issued Yubikey meaning it was locked.

I requested (and received) a refund for it but I wanted to see if I could brute force the lock code just for fun.

Running on an Intel MacBook Pro, I was getting ~11.4 tries per second
On a M1 Max, I was getting ~31.7 tries per second.

There are a total of `340282366920938463463374607431768211455` possible combinations for the lock code, even at 31.7 tries per second, it would take longer than the age of the universe to brute force. This was just a fun experiment to build.

### Usage:

Arguments:
`-t` How many threads. On Intel I used 8, on Apple Silicon I used 20.
`-s` Start number. Must be less than the end number.
`-e` End number.

I've implemented a start and an end number so that you can run this in managble batches.

Example:

`python bruteforce.py -t 20 -s 0 -e 1000000`
