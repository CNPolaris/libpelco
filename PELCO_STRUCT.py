class libpelco_structs:

    def __init__(self) -> None:
        # Frame format:		|synch byte|address|command1|command2|data1|data2|checksum|
        # Bytes 2 - 6 are Payload Bytes
        self._frame = {
            'synch_byte': 'FF',  # Synch Byte, always FF		-	1 byte
            'address': '00',  # Address			-	1 byte
            'command1': '00',  # Command1			-	1 byte
            'command2': '00',  # Command2			-	1 byte
            'data1': '00',  # Data1	(PAN SPEED):		-	1 byte
            'data2': '00',  # Data2	(TILT SPEED):		- 	1 byte 
            'checksum': '00'  # Checksum:			-       1 byte
        }
        # Format: Command Hex Code
        self._func = {
            'DOWN': '10',  # 下
            'UP': '08',  # 上
            'LEFT': '04',  # 左
            'RIGHT': '02',  # 右
            'UP-RIGHT': '0A',
            'DOWN-RIGHT': '12',
            'UP-LEFT': '0C',
            'DOWN-LEFT': '14',
            'STOP': '00',  # 停止
            'ZOOM_IN': '80',  # 焦距近
            'ZOOM_OUT': '01',  # 焦距远
            'LIGHT_ON': '0B',  # 灯光开
            'LIGHT_OFF': '09',  # 灯光关
            'F_BIG': '04',  # 光圈大
            'F_LITTLE': '02',  # 光圈小    
        }
