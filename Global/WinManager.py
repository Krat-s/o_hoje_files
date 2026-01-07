import ctypes
from pywinauto import Desktop

def check_windows() -> str:
    """
    Detecta corretamente se é Windows 10 ou 11 usando a API nativa.
    """
    class OSVERSIONINFOEXW(ctypes.Structure):
        _fields_ = [
            ("dwOSVersionInfoSize", ctypes.c_ulong),
            ("dwMajorVersion", ctypes.c_ulong),
            ("dwMinorVersion", ctypes.c_ulong),
            ("dwBuildNumber", ctypes.c_ulong),
            ("dwPlatformId", ctypes.c_ulong),
            ("szCSDVersion", ctypes.c_wchar * 128),
            ("wServicePackMajor", ctypes.c_ushort),
            ("wServicePackMinor", ctypes.c_ushort),
            ("wSuiteMask", ctypes.c_ushort),
            ("wProductType", ctypes.c_byte),
            ("wReserved", ctypes.c_byte),
        ]

    ver_info = OSVERSIONINFOEXW()
    ver_info.dwOSVersionInfoSize = ctypes.sizeof(OSVERSIONINFOEXW)

    ret = ctypes.windll.Ntdll.RtlGetVersion(ctypes.byref(ver_info))
    if ret != 0:
        return "Não foi possível detectar o Windows"

    major = ver_info.dwMajorVersion
    build = ver_info.dwBuildNumber

    if major == 10 and build >= 22000:
        print("Windows 11")
        return "Windows 11"
    elif major == 10:
        print("Windows 10")
        return "Windows 10"
    else:
        return f"Windows {major}"