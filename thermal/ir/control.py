__author__ = 'dan'

base_command = \
    '01111111 11110111 11111111 11111101 00000010\
    00000000 11111111 \
    11001100 00110011 \
    11100110 00011001 \
    00110111 11001000 \
    11{0}1   00{1}0   \
    11111111 00000000 \
    11111111 00000000 \
    11111111 00000000 \
    11111111 00000000 \
    11111111 00000000 \
    {2}{4}1  {3}{5}0  \
    0111{6}000 1000{7}111 \
    11111111 00000000 \
    11111111 00000000 \
    11111111 00000000 \
    00111111 110000000'

MODE_HEAT = '1001'
MODE_COOL = '0011'
MODE_DEHU = '0101'
MODE_AUTO = '0001'

FAN_0 = '011'
FAN_1 = '101'
FAN_2 = '001'
FAN_3 = '110'
FAN_A = '010'

POWER_ON = '0'
POWER_OFF = '1'

def bitflip(s):
    return s.replace('1','2').replace('0','1').replace('2','0')

def build_command(temperature, mode, fan, power):
    temperature = bin(temperature)[2:]
    temperature = bitflip(temperature)
    temperature = temperature[::-1] #reverse string

    command =  base_command.format(temperature, bitflip(temperature), mode, bitflip(mode), fan, bitflip(fan), power, bitflip(power))
    return command.replace(' ','')
