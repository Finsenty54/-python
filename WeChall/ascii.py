data='84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 105, 97, 114, 98, 111, 109, 97, 98, 99, 109, 109, 115'
datac=data.split(", ")

for i in datac:
    print(chr(int(i)),end='')
