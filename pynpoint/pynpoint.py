import ctypes
from typing import Optional, Tuple
import pathlib

class MCP:
    def __init__(self, port:str):
        if not isinstance(port, str):
            raise TypeError("port must be of type str!")
        self.port:str = port
        lib_path = pathlib.Path(__file__).parent.absolute() / "libmcp.so"
        self.lib = ctypes.CDLL(lib_path)
        self.handle: Optional[int] = None
        self._init()

    def _init(self) -> None:
        port = ctypes.c_char_p(self.port.encode())
        handle = self.lib.f511_init(port)
        if handle < 0:
            raise IOError(f"Got non negative return value from init function. ({handle})")
        self.handle = handle


    def get_power(self) -> Tuple[int, int]:
        if self.handle is None:
            raise IOError("Handle is not initialized!")
        
        channel1 = ctypes.c_int()
        channel2 = ctypes.c_int()
        result: int = self.lib.f511_get_power(ctypes.byref(channel1),
                 ctypes.byref(channel2), ctypes.c_int(self.handle))
        if result == 0:
            return channel1.value, channel2.value
        else:
            raise IOError(f"Got non zero return code ({result.value})!")
