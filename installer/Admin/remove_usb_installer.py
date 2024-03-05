import webbrowser  # internal module
import os,sys
from colorama import init, Fore # external package
import subprocess
import re
init(autoreset=True)

def main():
    print("        HephaestusOS维护系统 移除程序 FOSS")
    os.system("title HephaestusOS维护系统 移除程序-USB版")
    os.system("cls")
    print("        HephaestusOS维护系统 移除程序\n\n")
    while 1:
        adprint("您确实想要从您的USB驱动器中移除Hephaestus OS，及其附属的组件？",4)

        detect=input("[1]只移除Hephaestus OS,保留USB中的其他数据 [0]退出\n键入选项对应的数字，按Enter确认。\n>")
        if detect =="1":
            rcmd("cls")
            print("以下文件将被移除：\n    驱动器\\\\Hephaestus_OS.wim\n    驱动器\\\\Edgeless\n")
            adprint("现在，请输入制作好Hephaestus OS的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
            adprint("Hint:制作好的U盘卷标名应该叫Ventoy", 33)
            print("输入样例： H: ")
            detect = input()
            usb_path = ""
            if detect == "":
                adprint("未输入任何值！确认" + detectUsbPath() + "就是制作好的U盘吗？", 4)
                detect2 = input("[1]是这样的 [2]不是这样")
                if detect2 == "1":

                    usb_path = detectUsbPath()
                elif detect2 == "2":
                    rcmd("cls")
                    if detectUsbPath() is None:
                        adprint("出现错误！ 检测USB盘符时出现问题。")
                        print("确保插入了可移动驱动器，然后再试一次。")
                        return 1
                    adprint("现在，请输入制作好Hephaestus OS的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
                    adprint("Hint:制作好的U盘卷标名应该叫Ventoy", 33)
                    detect = input()
            else:
                print("输入的值是" + detect + "，这样没问题吗？")
                detect2 = ""
                detect2 = input("[1]是这样的 [2]不是这样")
                if detect2 == "1":
                    pattern = re.compile(r'^[A-Z]:$')
                    # 使用match方法检查字符串是否匹配
                    if pattern.match(detect):
                        if detectExist(detect) == 1:
                            adprint("要么输入的盘符不正确，要么u盘已经断开连接")
                            continue
                        usb_path = detect
                        break
                    else:
                        adprint("别凑热闹了，输入的都不是一个盘符")
                        continue
                else:
                    continue
            adprint("正在从"+usb_path+"中移除Hephaestus OS组件,保留USB驱动器内的其他文件...",4)
            rcmd("rmdir /s /q "+usb_path+"\\Edgeless")
            rcmd("del /f /q "+usb_path+"\\Hephaestus_OS.wim")
            rcmd("cls")
            adprint("移除完成。",22)
            '''
        elif detect=="2":
            rcmd("cls")
            adprint("现在，请输入制作好Hephaestus OS的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
            adprint("Hint:制作好的U盘卷标名应该叫Ventoy", 33)
            print("输入样例： H: ")
            detect = input()
            usb_path = ""
            if detect == "":
                adprint("未输入任何值！确认" + detectUsbPath() + "就是制作好的U盘吗？", 4)
                detect2 = input("[1]是这样的 [2]不是这样")
                if detect2 == "1":

                    usb_path = detectUsbPath()
                elif detect2 == "2":
                    rcmd("cls")
                    if detectUsbPath() is None:
                        adprint("出现错误！ 检测USB盘符时出现问题。")

                        return 1
                    adprint("现在，请输入制作好Hephaestus OS的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
                    adprint("Hint:制作好的U盘卷标名应该叫Ventoy", 33)
                    detect = input()
            else:
                print("输入的值是" + detect + "，这样没问题吗？")
                detect2 = ""
                detect2 = input("[1]是这样的 [2]不是这样")
                if detect2 == "1":
                    pattern = re.compile(r'^[A-Z]:$')
                    # 使用match方法检查字符串是否匹配
                    if pattern.match(detect):
                        if detectExist(detect) == 1:
                            adprint("要么输入的盘符不正确，要么u盘已经断开连接")
                            continue
                        usb_path = detect
                        break
                    else:
                        adprint("别凑热闹了，输入的都不是一个盘符")
                        continue
                else:
                    continue
            adprint("这将会会移除您USB存储上的任何文件，包括文档，媒体，程序和文件夹，并格式化它们！")
            adprint("您仍想要继续吗？",4)
            detect2=input("键入 yes 来继续。")
            if detect2 == "yes":
'''
        elif detect == "0":
            return 0










# external func ==========================================================

def ViewInBrowser(url: str):
    """
    在浏览器打开页面

    Args:
        url (str): 链接

    Returns:
        _type_: 1表示失败，None表示默认

        预期的结果应该是None
    """
    # this func used to open browser with a link (to download sth.)
    print("您即将前往访问", url, "正在打开浏览器...")
    try:
        webbrowser.open_new(url)
    except:
        adprint("出现错误，打开浏览器失败！", 1)
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


def detectExist(path: str):
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
    #result = p.stdout.read().decode('utf-8')
    result = p.stdout.read().decode('gbk')
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
            elif '可移动磁盘' in disk:
                return re.search(r'\w:', disk).group()
    '''#暂时没有面向linux posix开发的打算，就直接从自己以前的项目搬过来了
    elif os.name == 'posix':
        return sh('ll -a /media')[-1].strip()
    else:
        return sh('ls /Volumes')[-1].strip()
    '''


def rcmd(cmd: str, debug=0):
    if debug != 0:
        print("cd " + detectLocation() + " && " + cmd)
    ErrorCode = os.system(cmd)
    if ErrorCode != 0:
        adprint("执行语句" + cmd + "时发生了错误，", 1)
        return ErrorCode
    return 0


def adprint(text: str, color=0, enterln=True):
    """adprint print colorful text on screen 

    Args:
        enterln: return a line if not required, default is True, means will return a line after printed.
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
    11-light red
    22-light green
    33-light blue
    44-light yellow

    '''
    if color == 3:  # RG[B]
        print(Fore.BLUE + text, end="")
    elif color == 33:  # RG[B] ++
        print(Fore.LIGHTBLUE_EX + text, end="")
    elif color == 1:  # [R]GB
        print(Fore.RED + text, end="")
    elif color == 11:  # [R]GB++
        print(Fore.LIGHTRED_EX + text, end="")
    elif color == 2:  # R[G]B
        print(Fore.GREEN + text, end="")
    elif color == 22:  # R[G]B ++
        print(Fore.LIGHTGREEN_EX + text, end="")
    elif color == 4:  # yellow
        print(Fore.YELLOW + text, end="")
    elif color == 9:  # grey
        print(Fore.CYAN + text, end="")
    else:
        print(Fore.RED + text, end="")
    if enterln:
        print("", end="\n")
    return 0


# entry
if __name__ == "__main__":
    gpus = sys.argv
    # gpus = [int(gpus.split(','))]
    print(gpus)
    if gpus == ['remove_usb_installer.py', 'djlQok91BTI4D6F2pAt87IJFmsMxTXcy']:
        if main() != 0:
            #        raise Exception("An error occurred.")
            confirm()
    else:
        adprint("请不要直接运行脚本，这可能会引发问题。相反，请运行usb_install_entry.exe")
    rcmd("rmdir /s /q " + detectLocation() + "\\program\\")
