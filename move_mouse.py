import ctypes
import msvcrt
import time

def main():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print(key)
            if key == b'\x1b':
                break
        ctypes.windll.user32.SetCursorPos(100, 20)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
        time.sleep(5)

if __name__ == "__main__":
   main()