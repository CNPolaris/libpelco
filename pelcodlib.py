from PELCO_STRUCT import *


class PELCO_Functions():

    def __init__(self) -> None:
        self.pelco_struct = libpelco_structs()

    def __str__(self) -> str:
        return "This is Pelco D Ptz control lib"

    def _construct_cmd(self,
                       address='01',
                       cmd_1='00',
                       cmd_2='00',
                       pan_speed='00',
                       tilt_speed='00') -> bytes:
        """生成控制命令 

        Parameters
        ----------
        address : str, optional
            设备地址 16进制字符, by default '01'
        cmd_1 : str, optional
            指令1 16进制字符, by default '00'
        cmd_2 : str, optional
            指令2 16进制字符, by default '00'
        pan_speed : str, optional
            左右平移速度 16进制字符, by default '00'
        tilt_speed : str, optional
            上下平移速度 16进制字符, by default '00'
        
        Returns
        -------
        cmd : bytes
            生成最终的控制命令
        """
        self.pelco_struct._frame['address'] = address
        self.pelco_struct._frame['command1'] = cmd_1
        self.pelco_struct._frame['command2'] = cmd_2
        self.pelco_struct._frame['data1'] = pan_speed
        self.pelco_struct._frame['data2'] = tilt_speed
        self.pelco_struct._frame['checksum'] = self.checksum256(
            list(self.pelco_struct._frame.values())[1:-1])
        return self.pelco_struct.to_bytes()

    def checksum256(self, _str: list):
        """生成校验码 Byte2 到 Byte6 这 5 个数的和 (若超过 255 则除以 256 然后取余数 )

        Parameters
        ----------
        _str : list
            Byte2 到 Byte6

        Returns
        -------
        crc : str
            10进制的校验码
        """
        data_sum = 0
        for i in _str:
            data_sum += int(i, 16)
        return hex(data_sum % 256)[2:].zfill(2)

    def ptz_up(self, address='01', speed='FF'):
        """控制云台上扬

        Parameters
        ----------
        address : str, optional
            设备地址 16进制, by default '01'
        speed : str, optional
            移动速度 16进制 00~3F FF最高速, by default 'FF'
        
        Returns
        -------
        bytes
            0xff,0x01,0x00,0x08,0x00,0xff,0x08
        """
        func_code = self.pelco_struct._func['UP']
        return self._construct_cmd(address=address,
                                   cmd_2=func_code,
                                   tilt_speed=speed)

    def ptz_down(self, address='01', speed='FF'):
        func_code = self.pelco_struct._func['DOWN']
        return self._construct_cmd(address=address,
                                   cmd_2=func_code,
                                   tilt_speed=speed)

    def ptz_right(self, address='01', speed='FF'):
        func_code = self.pelco_struct._func['RIGHT']
        return self._construct_cmd(address=address,
                                   cmd_2=func_code,
                                   pan_speed=speed)

    def ptz_left(self, address='01', speed='FF'):
        func_code = self.pelco_struct._func['LEFT']
        return self._construct_cmd(address=address,
                                   cmd_2=func_code,
                                   pan_speed=speed)

    def ptz_stop(self, address='01'):
        func_code = self.pelco_struct._func['STOP']
        return self._construct_cmd(address=address, cmd_2=func_code)

    def zoom_in(self, address='01'):
        """焦距近

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        bytes
            _description_
        """
        func_code = self.pelco_struct._func['ZOOM_IN']
        return self._construct_cmd(address=address, cmd_2=func_code)

    def zoom_out(self, address='01'):
        """焦距远

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        bytes
            _description_
        """
        func_code = self.pelco_struct._func['ZOOM_OUT']
        return self._construct_cmd(address=address, cmd_1=func_code)

    def light_on(self, address='01'):
        """灯光开

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        bytes
            _description_
        """
        func_code = self.pelco_struct._func['LIGHT_ON']
        return self._construct_cmd(address=address,
                                   cmd_1=func_code,
                                   tilt_speed='01')

    def light_off(self, address='01'):
        """灯光关

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        bytes
            _description_
        """
        func_code = self.pelco_struct._func['LIGHT_OFF']
        return self._construct_cmd(address=address,
                                   cmd_1=func_code,
                                   tilt_speed='01')

    def f_big(self, address='01'):
        """光圈大

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        byts
            _description_
        """
        func_code = self.pelco_struct._func['F_BIG']
        return self._construct_cmd(address=address, cmd_1=func_code)

    def f_litle(self, address='01'):
        """光圈小

        Parameters
        ----------
        address : str, optional
            设备地址, by default '01'

        Returns
        -------
        bytes
            _description_
        """
        func_code = self.pelco_struct._func['F_LITTLE']
        return self._construct_cmd(address=address, cmd_1=func_code)
