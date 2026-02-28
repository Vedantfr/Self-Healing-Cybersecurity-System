<<<<<<< HEAD
import winreg

def add_to_startup():
    value = r'"C:\MajorProject\shcs\dist\main.exe" --agent'

    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(key, "SHCSAgent", 0, winreg.REG_SZ, value)
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_to_startup()

=======
import winreg

def add_to_startup():
    value = r'"C:\MajorProject\shcs\dist\main.exe" --agent'

    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(key, "SHCSAgent", 0, winreg.REG_SZ, value)
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_to_startup()

>>>>>>> ff48c825f9fd64ae919885467895d38972d81c36
