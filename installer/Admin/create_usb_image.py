import webbrowser  # internal module
import os,sys
from colorama import init, Fore
import subprocess
import re


init(autoreset=True)


# main action func
def main():
    # this script was used to install ventoy
    print("        HephaestusOS维护系统 安装程序 FOSS")
    os.system("title HephaestusOS维护系统 安装程序-USB版")
    os.system("cls")
    print("        HephaestusOS维护系统 安装程序\n\n")
    # debug option
    # print(__file__)
    # print(detectLocation())
    # debug end
    '''
    print(
        "首先，我们要从互联网上下载一个名叫Ventoy的便捷化USB引导设备制作工具。\n该工具的项目首页为https://www.ventoy.net/ \n您想现在下载它吗？\n[1]是，现在从互联网上下载 ["
        + "2]不，我想使用程序内置的版本 [0]关闭程序")
    detect = input()
    '''
    detect = "2"
    if detect == "1":  # 对~就应该从网上弄
        if ViewInBrowser("https://sourceforge.net/projects/ventoy/files/") == 1:
            adprint("你想再试一次吗？", 3)
            confirm()
            if ViewInBrowser("https://sourceforge.net/projects/ventoy/files/") == 1:
                print("仍然失败...")

                print("Errorloc:SYSTEM_WEBBROWSER_OPEN_FAIL")
                print("请检查您的系统环境是否异常或将其反馈给开发者，记得包括系统的详细信息。")
                return 1
        print(
            "请在打开的浏览器里面选取最新版本的Ventoy_1.0.97_windows.zip,然后将其下载下来。当下载完成后，请把zip文件直接拖入此窗口。")
        detect = ""
        detect = input()
        # detect = detect.replace("\\", "\\\\")
        print("正在解压...")
        if detectExist(detect) == 1:  # 查头
            # detect source failed
            print("无效路径！未能找到拖入的文件\n正在重试...")
            print(
                "请在打开的浏览器里面选取最新版本的Ventoy_1.0.97_windows.zip,然后将其下载下来。当下载完成后，请把zip文件直接拖入此窗口。")
            detect = ""
            detect = input()
            if detectExist(detect) == 1:
                print("仍然失败... :(")
                print("ErrorLoc:LOADIN_VENTOY_NOT_FOUND_1")
                print(
                    "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。")
                return 1

        ''' # obseleted
        if rcmd(detectLocation()+"\\source\\7z.exe e "+detect) !=0:
            #unzip error
            adprint("无法解压！",1)
            print("ErrorLoc:LOADIN_VENTOY_UNZIP_FAIL")
            adprint("请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",3)
            return 1
        '''

        if rcmd("mkdir " + detectLocation() + "\\program\\ventoy\\") != 0:  # 创标
            # mkdir system command fail
            adprint("创建文件夹失败！", 11)
            adprint("复制失败！", 11)
            adprint("参考上方报错，检查系统状态，或者重装此电脑，或者硬盘寿命已尽。", 9)
            adprint("程序将立刻终止。")
            print("wtf _HBBDKJSB_DEBUG_FLAG")
            return 1
        if rcmd("copy /v " + detect + " " + detectLocation() + "\\") != 0:  # 拷贝
            # copy failed
            adprint("复制失败！", 11)
            adprint("参考上方报错，检查系统状态，或者重装此电脑，或者硬盘寿命已尽。", 9)
            adprint("程序将立刻终止。")
            return 1
        if detectExist(detectLocation() + "\\ventoy-1.0.97-windows.zip") == 1:  # 查标
            # locate err
            adprint("定位文件失败！未能找到" + detectLocation() + "\\ventoy-1.0.97-windows.zip\n正在重试...", 1)
            if detectExist(".\\ventoy-1.0.97-windows.zip") == 1:
                adprint("仍然失败... :(", 3)
                print("ErrorLoc:LOCAL_VENTOY_NOT_FOUND_1")
                adprint(
                    "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
                    3)
                return 1
        if rcmd(detectLocation() + "\\source\\7z.exe x " + detectLocation() + "\\ventoy-1.0.97-windows.zip -o" + detectLocation() + "\\program\\ventoy\\") != 0:  # 解压
            # unzip error
            adprint("无法解压！", 1)
            print("ErrorLoc:LOCAL_VENTOY_UNZIP_FAIL")
            adprint(
                "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
                3)
            return 1
    elif detect == "2":  #
        rcmd("cls")
        print("正在解压...")
        # scr_path=detectLocation()
        # rcmd("cd "+detectLocation())
        if detectExist(detectLocation() + "\\source\\7z.exe") == 1:  # 查工具
            # unzip tool lost
            adprint("安装不完全！未能找到.\\source\\7z.exe\n正在重试...")
            if detectExist(".\\source\\7z.exe") == 1:
                adprint("仍然失败... :(")
                print("ErrorLoc:7Z_NOT_FOUND_1")
                adprint(
                    "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
                    3)
                return 1
        if detectExist(detectLocation() + "\\ventoy-1.0.97-windows.zip") == 1:  # 查标
            # internal ventoy lost
            adprint("安装不完全！未能找到.\\ventoy-1.0.97-windows.zip\n正在重试...", 1)
            if detectExist(".\\ventoy-1.0.97-windows.zip") == 1:
                adprint("仍然失败... :(", 3)
                print("ErrorLoc:LOCAL_VENTOY_NOT_FOUND_1")
                adprint(
                    "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
                    3)
                return 1
        if rcmd("mkdir " + detectLocation() + "\\program\\ventoy\\") != 0:  # 创标
            # mkdir system command fail
            adprint("创建文件夹失败！", 11)
            adprint("复制失败！", 11)
            print("wtf _JOISJI_FLAG_DEBUG")
            adprint("参考上方报错，检查系统状态，或者重装此电脑，或者硬盘寿命已尽。", 9)
            adprint("程序将立刻终止。")
            return 1
        if rcmd(detectLocation() + "\\source\\7z.exe x " + detectLocation() + "\\ventoy-1.0.97-windows.zip -o" + detectLocation() + "\\program\\ventoy\\") != 0:
            # unzip fail
            adprint("无法解压！", 1)
            print("ErrorLoc:LOCAL_VENTOY_UNZIP_FAIL")
            adprint(
                "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
                3)
            return 1
    elif detect == "0":
        return 0
    else:
        adprint("不合法的输入。执行默认操作：退出")
        return 0
    rcmd("cls")
    print("现在将打开ventoy安装程序，请按照界面指示插入一张空白U盘，然后按提示点击“安装”。")
    pass  # breakpoint
    items = os.listdir(detectLocation() + "\\program\\ventoy\\")
    folders = [item for item in items if os.path.isdir(item)]

    ventoy_location = detectLocation() + "\\program\\ventoy\\" + items[0] + "\\Ventoy2Disk.exe"
    if rcmd(ventoy_location) != 0:
        adprint("打开失败！", 11)
        rcmd("rmdir /q " + detectLocation() + "\\program\\ventoy")
    adprint(
        "完成安装后，按下任意键继续，但不要按显示屏上的按钮、键盘上的大小写切换或ctrl,win,shift键，也不是鼠标，更不是主机电源键！",
        22)
    # 因为内部测试有一堆人按奇奇怪怪的键然后告诉我没用，我真的 服~了QAQ
    confirm()
    rcmd("rmdir /s /q " + detectLocation() + "\\program\\ventoy")
    detect = None
    '''
    下面就是繁琐无谓的拷贝edgeless基础包了！好耶！1
    '''
    '''
    adprint("现在，请输入制作好usb引导的盘符，已经检测到的外置usb为"+detectUsbPath(),22)
    adprint("Hint:制作好的U盘卷标名应该叫Ventoy",33)
    print("输入样例： H: ")
    '''
    # detect=input()
    usb_path = ""
    while usb_path == "":
        rcmd("cls")
        if detectUsbPath() == None:
            adprint("出现错误！ 检测USB盘符时出现问题。")
        adprint("现在，请输入制作好usb引导的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
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
                if detectUsbPath() == None:
                    adprint("出现错误！ 检测USB盘符时出现问题。")

                    return 1
                adprint("现在，请输入制作好usb引导的盘符，已经检测到的外置usb为" + detectUsbPath(), 22)
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
    adprint("现在，请务必保持usb正常连接...", 4)
    if rcmd(detectLocation() + "\\source\\7z.exe x " + detectLocation() + "\\source\\compiled.7z -o" + usb_path) != 0:
        # unzip fail
        adprint("无法解压！", 1)
        print("ErrorLoc:LOCAL_SOURCE_UNZIP_FAIL")
        adprint(
            "请检查您的系统环境是否异常并尝试重新通过安装向导或附带的光盘进行安装，或将其反馈给开发者，记得包括系统的详细信息。",
            3)
        return 1
    rcmd("cls")
    adprint("成功安装！", 3)
    print(
        "Hephaestus OS 已经成功安装到你的U盘上。\n现在，将其插入关机的计算机上，然后在计算机启动时不断按下 F12 或 F7，选择USB启动即可打开Hephaestus OS。")
    confirm()
    return 0


'''Extended Func
'''


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


if __name__ == "__main__":
    gpus = sys.argv
    # gpus = [int(gpus.split(','))]
    print(gpus)
    if gpus == ['create_usb_image.py', 'C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG']:
        if main() != 0:
            #        raise Exception("An error occurred.")
            confirm()
    else:
        adprint("请不要直接运行脚本，这可能会引发问题。相反，请运行usb_install_entry.exe")
    rcmd("rmdir /s /q " + detectLocation() + "\\program\\")
