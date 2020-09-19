modes = ['ecb','cbc','cfb','ofb']
files = ['p31','p32','p33']

# encrypt
cmd = 'openssl enc -e -des-{} -nosalt -in {} -out {}{}.enc -pass file:pw'
for mode in modes:
    for file in files:
        print(cmd.format(mode,file,file,mode))

print('##########################################')
input("Copy above command to a different terminal to generate encrypted files.\nEnter to continue making error files...")
print('##########################################')
# make error
for mode in modes:
    for file in files:
        with open('{}{}.error.enc'.format(file,mode), 'wb') as error_file:
            with open('{}{}.enc'.format(file, mode), 'rb') as orig_file:
                byte = orig_file.read(1)
                counter = 0
                while byte != b"":
                    if counter == 71:
                        error_file.write(bytes([int(byte.hex(),16) ^ 0xff]))
                    else:
                        error_file.write(byte)
                    byte = orig_file.read(1)
                    counter += 1

# decrypt error
cmd = 'openssl enc -d -des-{} -nosalt -in {}{}.error.enc -out {}{}.error.dec -pass file:pw'
for mode in modes:
    for file in files:
        print(cmd.format(mode,file,mode,file,mode))


print('##########################################')
input("Copy above command to decrypt and compare.\nEnter to see differences...")
print('##########################################')

def compare_text(t1, t2):
    d1 = ''
    d2 = ''
    for i in range(len(t1)):
        if i >= len(t2):
            print('{}: {} '.format(i,t1[i:]))
            break
        elif t1[i] != t2[i]:
            d1 += t1[i]
            d2 += t2[i]
        elif t1[i] == t2[i] and d1 != '':
            print('{}: {} {}'.format(i-len(d1), d1, d2))
            d1 = ''
            d2 = ''
    if d1:
        print('{}: {} {}'.format(i - len(d1), d1, d2))
    if len(t2) > len(t1):
        print('{}:  {}'.format(len(t2)-len(t1), t2[len(t1):]))

for file in files:
    with open(file) as orig_file:
        orig_text = orig_file.readline()
        for mode in modes:
            print('------------------')
            print('diff {} {}{}.error.dec'.format(file, file, mode))
            with open('{}{}.error.dec'.format(file, mode),errors='replace') as error_file:
                error_text = error_file.readline()
                compare_text(orig_text, error_text)