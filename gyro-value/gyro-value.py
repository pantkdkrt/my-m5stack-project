from m5stack import *
from m5ui import *
from uiflow import *
import imu

setScreenColor(0x222222)

imu0 = imu.IMU()
x = M5TextBox(140,35,"X",lcd.FONT_DejaVu56,0xFFFFFF, rotate=0)

x.setText(str(imu0.gyro[0]))