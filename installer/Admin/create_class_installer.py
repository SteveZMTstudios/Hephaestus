#post-fs-data
import webbrowser #internal module
import os
from colorama import init,Fore
init(autoreset=True)
#end

#main action
def main():
    pass


'''Entended Func
'''
def ViewInBrowser(url:str):
    # this func used to open browser with a link (to download sth.)
    print("您即将前往访问",url,"正在打开浏览器...")
    try:
        webbrowser.open_new(url)
    except:
        adprint("出现错误，打开浏览器失败！",1)
        return 1
    return None

def confirm():
    os.system("pause")
    # anykey=input("[Anykey]继续")

#return this script's location
def detectLocation():
    script_path = __file__
    script_directory = os.path.dirname(script_path)
    return script_directory

#detect file is exist or not
def detectExist(path:str):
    if os.path.exists(path):
        return 0
    else:
        return 1

#running cmd on shell or Powershell or cmd
def rcmd(cmd:str):
    ErrorCode=os.system(cmd)
    if ErrorCode != 0:
        adprint("执行语句"+cmd+"时发生了错误，",1)
        return ErrorCode
    return 0

#colorful printout 
def adprint(text:str,color=0,enterln=True):
    """adprint print colorful text on screen 

    Args:
        text (str): input any str as you want
        color (int, optional): _see also available color. Defaults to 0(red).
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
    '''
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

# Program Entry
if __name__ == "__main__" :
    if main() != 0:
#        raise Exception("An error occured.")
        confirm()