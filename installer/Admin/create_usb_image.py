import webbrowser #internal module
import os

def main():
    # this script was used to install ventoy
    print("        HephaestusOS维护系统 安装程序")
    os.system("title 'Hephaestus Installer For USB disk'")
    os.system("cls")
    print("        HephaestusOS维护系统 安装程序\n\n")
    print("首先，我们要从互联网上下载一个名叫Ventoy的便捷化USB引导设备制作工具。\n该工具的项目首页为https://www.ventoy.net/ \n您想现在下载它吗？\n[1]是，现在从互联网上下载 [2]不，我想使用程序内置的版本")
    detect=input()
    if detect == "1":
        if ViewInBrowser("https://sourceforge.net/projects/ventoy/files/v1.0.97") == 1:
            print("你想再试一次吗？")
            confirm()
            if ViewInBrowser("https://sourceforge.net/projects/ventoy/files/v1.0.97") == 1:
                print("仍然失败...")
                print("Error locate:SYSTEM_WEBBROWSER_OPEN_FAIL")
                print("请检查您的系统环境是否异常或将其反馈给开发者，记得包括系统的详细信息。")
                return 1
        print("请在打开的浏览器里面选取最新版本的Ventoy_1.0.97_windows.zip,然后将其下载下来。当下载完成后，请把zip文件直接拖入此窗口。")
        detect=""
        detect=input()
    elif detect == "2":
        print("正在解压...")
        scr_path=detectLocation()[0]




def ViewInBrowser(url):
    # this func used to open browser with a link (to download sth.)
    print("您即将前往访问",url,"正在打开浏览器...")
    try:
        webbrowser.open_new(url)
    except:
        print("出现错误，打开浏览器失败！")
        return 1
    return None

def confirm():
    os.system("pause")

def detectLocation():
    script_path = __file__
    script_directory = os.path.dirname(script_path)
    return [script_directory,script_path]

def detectExist(path):
    if os.path.exists(path):
        return 0
    else:
        return 1



if __name__ == "__main__" :
    if main() != 0:
#        raise Exception("An error occured.")
        pass