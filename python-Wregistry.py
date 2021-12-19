import winreg
import ctypes


choice = int(input("Quelle exercice : 1 startup programme : 2 bloquer USB ; 3 Lister les Wifi : "))




def Persistence():
    #TODO
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0, winreg.KEY_SET_VALUE)
    with reg_key:
        winreg.SetValueEx(reg_key, 'calc', 0, winreg.REG_SZ, '"C:\Windows\System32\calc.exe"')

def WifiList():
    #TODO
    print("Liste des WIFI qui ce sont deja connecter à cette machine :")
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles", 0, winreg.KEY_READ)
    for i in range(0, winreg.QueryInfoKey(key)[0]):
        skey_name = winreg.EnumKey(key, i)
        skey = winreg.OpenKey(key, skey_name)
        try:
            a = winreg.QueryValueEx(skey, 'ProfileName')[0]
            b = winreg.QueryValueEx(skey, 'NameType')[0]
            if b == 71:
                print(a)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(None, e, u"Fatal Error", 0)
            pass
        finally:
            skey.Close()

def UsbBlock():
    #TODO
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SYSTEM\CurrentControlSet\Services\USBSTOR',0,winreg.KEY_SET_VALUE)
    with reg_key:
        winreg.SetValueEx(reg_key, 'start', 1, winreg.REG_DWORD, 4)


if choice == 1:
    Persistence()

if choice == 3:
    WifiList()

if choice == 2:
    UsbBlock()
