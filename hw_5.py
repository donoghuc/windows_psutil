import psutil
import win32api
import sys
import os

def menu():
    '''Give directions on command prompt'''
    menu = """Choose from enumeration below
1. Enumerate Running Processes
2. List all Running Threads Within Process
3. Enumerate Loaded Modules
4. Show Executable Pages
5. Read Memory
6. 6, q or Q to quit
>>"""
    return menu


def quit(command):
    ''' test for quit command'''
    quit_command = set(('6','q','Q'))
    if command in quit_command:
        return True
    return False


def validate_command(command):
    ''' test for valid input string'''
    valid = set(('1','2','3','4','5','6','q','Q'))
    if command in valid:
        return True
    return False


def proc_1():
    '''Enumerate all the running processes.'''
    proc_list = list()
    max_str = dict(idx=0,pid=0,name=0,username=0)
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        max_str['pid'] = len(str(proc.info['pid'])) if len(str(proc.info['pid'])) > max_str['pid'] else max_str['pid']
        max_str['name'] = len(str(proc.info['name'])) if len(str(proc.info['name'])) > max_str['name'] else max_str['name']
        max_str['username'] = len(str(proc.info['username'])) if len(str(proc.info['username'])) > max_str['username'] else max_str['username']
        proc_list.append(proc.info)
    max_str['idx'] = len(str(len(proc_list))) if len('INDEX') < len(str(len(proc_list))) else len('INDEX')
    print("{0:{idx}} | {1:{pid}} | {2:{name}} | {3:{uname}} ".format('INDEX','PID','NAME','USERNAME',idx=max_str['idx'],
                                                            pid=max_str['pid'],name=max_str['name'],uname=max_str['username']))
    for i,pro in enumerate(proc_list):
        print("{0:{idx}} | {1:{pid}} | {2:{name}} | {3:{uname}} ".format(i,str(pro['pid']),str(pro['name']),str(pro['username']),idx=max_str['idx'],
                                                            pid=max_str['pid'],name=max_str['name'],uname=max_str['username']))


def proc_2():
    '''List all the running threads within process boundary'''
    user_proc = input("Enter ProcessID to see threads for. \n>>")
    try:
        proc = psutil.Process(int(user_proc))
        print(proc)
        print("{} | {} | {}".format("TRD ID", "USER TIME", "SYSTEM TIME"))
        for trd in proc.threads():
            print("{:6} | {:9.3f} | {:9.3f}".format(trd.id, trd.user_time, trd.system_time))
    except:
        print("Invalid PID")


def proc_3():
    '''Enumerate all the loaded modules within the processes'''
    user_proc = input("Enter ProcessID to see loaded modules for. \n>>")
    try:
        p = psutil.Process(int(user_proc))
        # print(p)
        print("{:6} | {:25}".format("INDEX", "LOADED MODULES PATH"))
        for idx, dll in enumerate(p.memory_maps()):
            print("{:6} | {:25}".format(idx, dll.path))
            # print(dll.path)
    except:
        print("Invalid PID")


def proc_5():
    '''Enumerate all the loaded modules within the processes'''
    # p = psutil.Process( os.getpid() )
    # from ctypes import *
    # from ctypes.wintypes import *

    # OpenProcess = windll.kernel32.OpenProcess
    # ReadProcessMemory = windll.kernel32.ReadProcessMemory
    # CloseHandle = windll.kernel32.CloseHandle

    # PROCESS_ALL_ACCESS = 0x1F0FFF

    # pid = os.getpid()   # I assume you have this from somewhere.
    # address = 0x1000000  # Likewise; for illustration I'll get the .exe header.

    # buffer = c_char_p("The data goes here")
    # bufferSize = len(buffer.value)
    # bytesRead = c_ulong(0)

    # processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    # if ReadProcessMemory(processHandle, address, buffer, bufferSize, byref(bytesRead)):
    #     print "Success:", buffer
    # else:
    #     print "Failed."
    
    # print(list(psutil.win_service_iter()))
    # print(psutil.win_service_get('python.exe'))

    import ctypes, win32ui, win32process ,win32api, win32con
    from ctypes import wintypes

    # PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
    # HWND = win32ui.FindWindow(None,"Solitär").GetSafeHwnd()
    # print(HWND)
    # PID = win32process.GetWindowThreadProcessId(HWND)[1]
    rPM = ctypes.WinDLL('kernel32',use_last_error=True).ReadProcessMemory
    rPM.argtypes = [wintypes.HANDLE,wintypes.LPCVOID,wintypes.LPVOID,ctypes.c_size_t,ctypes.POINTER(ctypes.c_size_t)]
    rPM.restype = wintypes.BOOL
    pids = [proc.info['pid'] for proc in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    for p in pids:
        try:
            print(p)
            PID = int(p)
            # print(PID)
            PROCESS = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS,0,PID)
            ADDRESS1 = 0x00000000
            ADDRESS2 = ctypes.create_string_buffer(64)
            bytes_read = ctypes.c_size_t()
            print(rPM(PROCESS.handle,ADDRESS1,ADDRESS2,64,ctypes.byref(bytes_read)))
            print(repr(PROCESS))
            print(ctypes.get_last_error())
            print(ADDRESS2.value)
        except:
            print("nope ",p)


def proc_4():
    ''' load page and address info'''
    user_proc = input("Enter ProcessID to see executable pages for. \n>>")
    p = psutil.Process(int(user_proc))
    try:
        print("{:13} | {:25} | {:10}".format("BASE ADDRESS", "NAME", "RESIDENT SET SIZE"))
        for dll in p.memory_maps():
            try:
                print("{:13x} | {:25} | {:10}".format(win32api.GetModuleHandle(dll.path), dll.path.split(os.sep)[-1], dll.rss))
            except:
                pass
    except:
        print("Invalid PID")

def main():
    ''' main logic for HW_5 prog'''
    command = False
    while not quit(command):
        command = input(menu())
        while not validate_command(command):
            print("Invalid Command: {}".format(command))
            command = input(menu())

        if command == '1':
            proc_1()
        if command == '2':
            proc_2()
        if command == '3':
            proc_3()
        if command == '4':
            proc_4()
        if command == '5':
            proc_5()

if __name__ == '__main__':
    main()




