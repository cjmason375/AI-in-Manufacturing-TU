from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client import ModbusSerialClient as ModbusClient
import datetime
import time

# define client object: Modbus RTU
# check your port.
# how do you find out what port you are connected to??
client = ModbusClient(method='rtu', port='/dev/tty.usbserial-A10KNI0B', timeout=1, stopbits=1, bytesize=8, parity='N', baudrate=57600, strict=False)

# client connect to communicate
client.connect()

# reading register method - decoding byte array
def read_register(ADDR, COUNT, UNIT):
    rr = client.read_holding_registers(ADDR, COUNT, slave=UNIT)
    decoder = BinaryPayloadDecoder.fromRegisters(rr.registers, byteorder=Endian.BIG, wordorder=Endian.BIG)
    return decoder.decode_32bit_float()

now = datetime.datetime.now()

# for the table, please see the link below (Purdue ME597-IIoT impl for smrt mfg)
# https://colab.research.google.com/github/purduelamm/purdue_me597_iiot/blob/main/lab/lab3/L3_Colab2.ipynb#scrollTo=YStzgYT8unk7

# this is a total power consumption parameter: Address 1564-1565 (061CH-061DH)
# below are some more parameters you could try.
# voltage = read_register(1538, 2, 1) # this is phase 1 voltage parameter: Address 1538-1538 (0602H-0603H)
# current = read_register(1550, 2, 1) # this is phase A current parameter: Address 1550-1551 (060EH-060FH)

while True: # infinite loop
    power = read_register(1564, COUNT=2, UNIT=1) # Total true power in Watt
    print("{}: Total power consumption is {} W.".format(now, power))
    # try to print out voltage and current
    
    time.sleep(1) # time sleep for 1 sec.
    # To halt program, please hit CTRL+C

client.close()



