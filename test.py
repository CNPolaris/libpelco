import serial
import time
from pelcodlib import PELCO_Functions

# 使用485串口 波特率9600 设备地址1
ser = serial.Serial("COM3", 9600)
pelco = PELCO_Functions()

# 测试上扬
print("=" * 20 + "测试上扬" + "=" * 20)
ser.write(pelco.ptz_up())
time.sleep(5)
ser.write(pelco.ptz_stop())

# 测试下降
print("=" * 20 + "测试下降" + "=" * 20)
ser.write(pelco.ptz_down())
time.sleep(5)
ser.write(pelco.ptz_stop())

# 测试左转
print("=" * 20 + "测试左转" + "=" * 20)
ser.write(pelco.ptz_left())
time.sleep(5)
ser.write(pelco.ptz_stop())

# 测试右转
print("=" * 20 + "测试右转" + "=" * 20)
ser.write(pelco.ptz_right())
time.sleep(5)
ser.write(pelco.ptz_stop())

# 测试焦距放近
print("=" * 20 + "测试焦距放近" + "=" * 20)
ser.write(pelco.zoom_in())
time.sleep(5)
ser.write(pelco.ptz_stop())

# 测试焦距放远
print("=" * 20 + "测试焦距放远" + "=" * 20)
ser.write(pelco.zoom_out())
time.sleep(5)
ser.write(pelco.ptz_stop())
