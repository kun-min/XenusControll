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
        ser.write(trans("s r0xca "+str(positon)+"\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcb 400000\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcc 400000\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0xcd 200000\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("s r0x24 21\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
        ser.write(trans("t 1\n"))  # 訊息必須是位元組類型
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
        ser.write(trans("s r0x24 0\n"))  # 訊息必須是位元組類型
        check(ser)
        sleep(0.1)
    except KeyboardInterrupt:
        ser.close()
        print('再見！')