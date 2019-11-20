# 1
print('Part (1)')
with open ('weather.csv', 'r') as reader:
    data=reader.read()
print (data)

# 2
print('Part (2)')
with open ('weather.csv', 'r') as reader:
    line=reader.readline()
    while line != '':
        line=reader.readline()
        print(line)
    print("It's over")

# 3
print('Part (3)')
with open ('weather.csv', 'r') as reader:
    line1=reader.readline()
    rain=[]
    for line in reader.readlines():
        print(line)
        rain1=line.split(',')
        rain2=float(rain1[-1])
        rain.append(rain2)
    print (rain)

with open ('myrain.txt', 'w') as writer:
    for item in rain:
        writer.write(str(item) + '\n')

# 4
import struct #import stuck module
bin_data=struct.pack('bbbb',123,12,45,34)
with open ('mybinary.dat', 'wb') as bwriter:
    bwriter.write(bin_data)

with open ('mybinary.dat', 'rb') as breader:
    bin_data2=breader.read()


