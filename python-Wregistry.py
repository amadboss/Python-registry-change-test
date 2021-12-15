import winreg
import ctypes
import os
import errno
choise = int(input("Quelle exercice : 1 startup programme : 2 bloquer USB ; 3 Lister les Wifi : "))

    
    

if choise == 1:
    
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0, winreg.KEY_SET_VALUE)
    with reg_key:
        winreg.SetValueEx(reg_key, 'calc', 0, winreg.REG_SZ, '"C:\Windows\System32\calc.exe"')

if choise == 2:
    
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SYSTEM\CurrentControlSet\Services\USBSTOR',0,winreg.KEY_SET_VALUE)
    with reg_key:
        winreg.SetValueEx(reg_key, 'start', 1, winreg.REG_DWORD, 4)

if choise == 3:
    
    print("Liste of WIFI qui ce sont deja connecter a cette machine :")
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles", 0, winreg.KEY_READ)
    for i in range(0, winreg.QueryInfoKey(key)[0]):
        skey_name = winreg.EnumKey(key, i)
        skey = winreg.OpenKey(key, skey_name)
        try:
            a = winreg.QueryValueEx(skey, 'ProfileName')[0]
            b = winreg.QueryValueEx(skey, 'NameType')[0]
            if b == 71:
                print(a)
        except OSError as e:
            if e.errno == errno.ENOENT:
                pass
        finally:
            skey.Close()
    
