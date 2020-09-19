from p2_data import data, indexed_data
import pickle

lookup_tbl = [[0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0],
              [0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8],
              [0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3],
              [0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb],
              [0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa],
              [0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5],
              [0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf],
              [0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd],
              [0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc],
              [0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4],
              [0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe],
              [0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7],
              [0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6],
              [0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2],
              [0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9],
              [0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1]]

input_file = open('../../../assignment1_nonsliding/ciphertext2', 'rb')
byte = input_file.read(1)

### Prepare some data ###
try:
    with open('p2_sequence', 'rb') as data:
        sequence = pickle.load(data)
    with open('p2_hex', 'rb') as data:
        hex_sequence = pickle.load(data)
except:
    sequence = []
    hex_sequence = []

    while byte != b"":
        hex_code = byte.hex()
        cl = hex_code[-1]
        ch = hex_code[-2] if hex_code[-2] != 'x' else '0'

        ph_kl = []
        pl_kh = []
        possible_p_k = {}
        for row in range(len(lookup_tbl)):
            for cell in range(len(lookup_tbl[row])):

                if lookup_tbl[row][cell] == int(ch, 16):
                    ph_kl.append((hex(row).replace('0x', ''), hex(cell).replace('0x', '')))

                if lookup_tbl[row][cell] == int(cl, 16):
                    pl_kh.append((hex(row).replace('0x', ''), hex(cell).replace('0x', '')))

        for ph, kl in ph_kl:
            for pl, kh in pl_kh:
                p_ascii = int(ph + pl, 16)
                # if p_ascii < 32 or p_ascii >= 127: continue
                k_ascii = int(kh + kl, 16)
                if k_ascii < 32 or k_ascii >= 127: continue
                possible_p_k[chr(k_ascii)] = p_ascii

        sequence.append(possible_p_k)
        hex_sequence.append(hex_code)

        byte = input_file.read(1)

    with open('p2_sequence', 'wb') as file:
        pickle.dump(sequence, file, pickle.HIGHEST_PROTOCOL)
    with open('p2_hex', 'wb') as file:
        pickle.dump(hex_sequence, file, pickle.HIGHEST_PROTOCOL)

### Finding key length ###
search_len = 1000
for step in range(1, 100):
    match = total = 0
    for i in range(search_len):
        for j in range(i + step, search_len, step):
            total += 1
            if hex_sequence[i] == hex_sequence[j]: match += 1

    ioc = float(match) / float(total)

    print("%3d%7.2f%% %s" % (step, 100*ioc, "#" * int(0.5 + 500*ioc)))

### Loke for file type ###
for signature in indexed_data:
    key_string = ''
    bits = signature.lower().split()
    for i in range(len(bits)):
        found = False
        bit = bits[i]
        if bit == '??': continue
        try:offset = int(indexed_data[signature]['offset'])
        except: offset = 0
        for key in sequence[i + offset]:
            if sequence[i + offset][key] == int(bit, 16):
                key_string += key
                found = True
                break
        if not found:
            key_string = ''
            break
    if key_string:
        print(signature, indexed_data[signature]['type'], key_string)

### Finding end of central directory ###
dt = {i:{} for i in range(40)}
for i in range(len(hex_sequence)-1000,len(hex_sequence)-3):
    key_string = ''
    for key in sequence[i]:
        if sequence[i][key] == int('50', 16):
            key_string += key
    for key in sequence[i+1]:
        if sequence[i+1][key] == int('4b', 16):
            key_string += key
    for key in sequence[i+2]:
        if sequence[i+2][key] == int('05', 16):
            key_string += key
    for key in sequence[i+3]:
        if sequence[i+3][key] == int('06', 16):
            key_string += key
    if len(key_string) == 4:
        try:dt[i%40][key_string].append(i)
        except: dt[i%40][key_string] = [i]
for i in sorted(dt.keys()):
    for key in sorted(dt[i].keys(),key=lambda x: len(dt[i][x])):
        print('0506', i, key, dt[i][key])
# 0506: 131882

### Finding central directory ###
dt = {i:{} for i in range(40)}
for i in range(131682,131882):
    key_string = ''
    for key in sequence[i]:
        if sequence[i][key] == int('50', 16):
            key_string += key
    for key in sequence[i+1]:
        if sequence[i+1][key] == int('4b', 16):
            key_string += key
    for key in sequence[i+2]:
        if sequence[i+2][key] == int('01', 16):
            key_string += key
    for key in sequence[i+3]:
        if sequence[i+3][key] == int('02', 16):
            key_string += key
    if len(key_string) == 4:
        try:dt[i%40][key_string].append(i)
        except: dt[i%40][key_string] = [i]
for i in sorted(dt.keys()):
    for key in sorted(dt[i].keys(),key=lambda x: len(dt[i][x])):
        print('0102', i, key, dt[i][key])
# 0102: 131823

### Look for key at a position ###
# Enter hex code and position to see if there is any key can decrypt resulting in that hex code at that position
while True:
    bit, pos = input('> ').split()
    if pos == '-1': break
    found = False
    for key in sequence[int(pos)]:
        if sequence[int(pos)][key] == int(bit, 16):
            print(key)
            found = True
    if not found:
        print([ (k, chr(sequence[int(pos)][k])) for k in sequence[int(pos)] ] )

### Decrypt resulted key ###
def decipher(key):
    fn = 'p2.zip'

    with open(fn, 'wb') as out_file:
        for i in range(len(sequence)):
            out_file.write(bytes([sequence[i][ key[i%len(key)] ] ]))
    return fn

decipher('[95wJL4PiE)7u^P-Q(%^-_254dh1F@@nnE128eRo')