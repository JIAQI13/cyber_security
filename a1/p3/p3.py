input_file = open('../../../assignment1_nonsliding/ciphertext3', 'rb')
# input_file = open('testfile.enc', 'rb')
byte = input_file.read(1)

sequence = []
hex_sequence = []

while byte != b"":
    hex_code = byte.hex()
    hex_sequence.append(int(hex_code, 16))
    byte = input_file.read(1)

seq_len = len(hex_sequence) // 12
tmp = []
while hex_sequence:
    if len(tmp) < seq_len:
        tmp.append(hex_sequence.pop(0))
    else:
        sequence.append(tmp[:])
        tmp = []

if tmp:
    sequence.append(tmp)

with open('p3.out', 'wb') as out_file:
    out_file.write(bytes(sequence.pop(3)))
    for seq in sequence:
        out_file.write(bytes(seq))

input_file.close()