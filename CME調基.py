
import serial
from time import sleep
import sys

COM_PORT = 'COM6'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values
message = []
flag = 0
try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        #choice = input('按1開燈、按2關燈、按e關閉程式  ').lower()
        #cmd = encode("g r0x32\n")
        cmd = "s r0xc8 0\n"
        data = bytes(to_ascii(cmd))
        ser.write(data)  # 訊息必須是位元組類型
        sleep(1)
        while ser.in_waiting:
            #print("Feedback")
            mcu_feedback = ser.read_until(b'\r').decode()  # 接收回應訊息並解碼
            a = "ok"
            print(mcu_feedback[0:2] == 'ok')





except KeyboardInterrupt:
    ser.close()
    print('再見！')