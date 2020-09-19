import itertools

for numlen in range(8,-1,-1):
    for v in itertools.product('1234567890abcdef', repeat=numlen):
        num = ''.join(v)
        print(num)
        print(num.upper())
