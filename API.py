from time import sleep
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values
def check(ser):
    while ser.in_waiting:
        mcu_feedback = ser.read_until(b'\r').decode()  # 接收回應訊息並解碼
        if(mcu_feedback[0:2] == 'ok'):
            pass
        else:
            print("Comand Error")
            break
def trans(cmd):
    return bytes(to_ascii(cmd))

def go(positon,ser):
    try:
        ser.write(trans("s r0xc8 0\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xca "+str(positon)+"\n"))  # 設定位置
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcb "+str(400000)+"\n"))  # Set maximum velocity to 400000 counts/second.
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcc "+str(400000)+"\n"))  # Set maximum acceleration to 400000 counts/second2.
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcd "+str(200000)+"\n"))  # Set maximum deceleration to 2000000 counts/second2
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0x24 21\n"))  # Enable the drive in Programmed Position (Trajectory Generator) Mode.
        check(ser)
        sleep(0.1)
        ser.write(trans("t 1\n"))  #Execute the move.
        check(ser)
        sleep(0.1)
    except KeyboardInterrupt:
        ser.close()
        print('再見！')

def enable(ser):
    try:
        ser.write(trans("s r0x24 1\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
    except KeyboardInterrupt:
        ser.close()
        print('再見！')
def disable(ser):
    try:
        ser.write(trans("s r0x24 0\n"))  # disable
        check(ser)
        sleep(0.1)
    except KeyboardInterrupt:
        ser.close()
        print('再見！')

def read_current(ser):
    try:
        ser.write(trans("g r0x0c\n"))  # Reads actual current output from the drive.
        check(ser)
        sleep(0.1)
        while ser.in_waiting:
            mcu_feedback = ser.read_until(b'\r').decode()  # 接收回應訊息並解碼
            print(mcu_feedback)
    except KeyboardInterrupt:
        ser.close()
        print('再見！')
