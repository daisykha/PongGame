import smbus
import time
I2C_ADDR = 0x20
PORT_ON = 0xFF
bus = smbus.SMBus(1)
bus.write_byte( I2C_ADDR, PORT_ON )

while True:                        
     i2cvalue = bus.read_byte( I2C_ADDR )      
     time.sleep(1)

while True:
    if 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 10 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
    elif 0 < ball.GetPositionX and ball.GetPositionX <= 10:
