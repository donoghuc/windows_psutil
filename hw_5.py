import psutil
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
    for proc in psutil.process_iter():
        try:
            print(proc.threads())
        except:
            print("no access")


def proc_3():
    '''Enumerate all the loaded modules within the processes'''
    p = psutil.Process( os.getpid() )
    print(p)
    for dll in p.memory_maps():
        print(dll.path)


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

if __name__ == '__main__':
    main()




