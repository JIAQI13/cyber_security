import itertools, threading, time

LENGTH = 4  # Length of number
SEP_LIST = [''] + list('!@#$%^&*()_+~`-=;\'\\|,.<>?:"')   # Add empty string for noseparator
APPEND = True

def outfunc(sep):
    for tail in itertools.product('1234567890', repeat=LENGTH):
        if APPEND: print(sep + ''.join(tail))
        else: print(''.join(tail) + sep)

threads = []

for sep in SEP_LIST:
    t = threading.Thread(
        target=outfunc,
        args=(sep)
    )
    threads.append(t)
    t.start()

while any(t.is_alive() for t in threads):
    time.sleep(1)