import webbrowser #internal module
import os
from colorama import init,Fore
import subprocess
import re
init(autoreset=True)

'''Extended Func
'''

def ViewInBrowser(url:str):
    """
    在浏览器打开页面

    Args:
        url (str): 链接

    Returns:
        _type_: 1表示失败，None表示默认

        预期的结果应该是None
    """
    # this func used to open browser with a link (to download sth.)
    print("您即将前往访问",url,"正在打开浏览器...")
    try:
        webbrowser.open_new(url)
    except:
        adprint("出现错误，打开浏览器失败！",1)
        return 1
    return None

def confirm():
    """_summary_

    让用户按下任意键继续
    """
    os.system("pause")
    # anykey=input("[Anykey]继续")

def detectLocation():
    script_path = __file__
    script_directory = os.path.dirname(script_path)
    return script_directory

def detectExist(path:str):
    if os.path.exists(path):
        return 0
    else:
        return 1


def sh(command, print_msg=True):
    """_summary_
        get output and also get stdout tool, use Popen

    Args:
        command (_type_): 运行的命令
        print_msg (bool, optional): 要不要打到屏幕 Defaults to True.

    Returns:
        _type_: 返回命令结果
    """
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def detectUsbPath():
    """检测插入usb盘符

    Returns:
        _type_: 盘符
    """
    if os.name == 'nt':
        disks = sh("wmic logicaldisk get deviceid, description",
                   print_msg=False).split('\n')
        for disk in disks:
            if 'Removable' in disk:
                return re.search(r'\w:', disk).group()
    '''#暂时没有面向linux posix开发的打算，就直接从自己以前的项目搬过来了
    elif os.name == 'posix':
        return sh('ll -a /media')[-1].strip()
    else:
        return sh('ls /Volumes')[-1].strip()
    '''


def rcmd(cmd:str,debug=0):
    if debug != 0:
        print(cmd)
    ErrorCode=os.system(cmd)
    if ErrorCode != 0:
        adprint("执行语句"+cmd+"时发生了错误，",1)
        return ErrorCode
    return 0

def adprint(text:str,color=0,enterln=True):
    """adprint print colorful text on screen 

    Args:
        text (str): input any str as you want
        color (int, optional): _see also available color. Defaults to 0(red).
        Available color
    [None] = 1 -Red
    1-Red
    2-Blue
    3-Green
    4-yellow
    11-lightred
    22-lightgreen
    33-lightblue
    44-lightyellow

        enterln (bool, optional): require anotherline or not. Defaults to True.

    Returns:
        _type_: None
    """    '''
    Available color
    [None] = 1 -Red
    1-Red
    2-Blue
    3-Green
    4-yellow
    11-lightred
    22-lightgreen
    33-lightblue
    44-lightyellow

    '''
    if color == 3:# RG[B]
        print(Fore.BLUE+text,end="")
    elif color == 33:# RG[B] ++
        print(Fore.LIGHTBLUE_EX+text,end="")
    elif color == 1:#[R]GB
        print(Fore.RED+text,end="")
    elif color == 11:#[R]GB++
        print(Fore.LIGHTRED_EX+text,end="")
    elif color == 2:#R[G]B
        print(Fore.GREEN+text,end="")
    elif color == 22:#R[G]B ++
        print(Fore.LIGHTGREEN_EX+text,end="")
    elif color == 4:#yellow
        print(Fore.YELLOW+text,end="")
    elif color == 9:#grey
        print(Fore.CYAN+text,end="")
    else:
        print(Fore.RED+text,end="")
    if enterln == True:
        print("",end="\n")
    return 0

if __name__ == "__main__" :
    print(detectLocation())
