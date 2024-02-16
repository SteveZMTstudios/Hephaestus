@echo off
setlocal enabledelayedexpansion

set URL="http://192.168.0.1"
set OUTPUT_DIR=".\"
set JSON_TEMPLATE='{"mgr_ip": "%IP%", "token": "%TOKEN%", "": 30, "city": "New York"}'

::for /f "tokens=*" %%A in ('ipconfig ^| findstr /i "IPv4 Address"') do set IP=%%A

for /f "tokens=15 delims=:" %%i in ('ipconfig /all ^| findstr /i "IPv4 Address"') do (
    set "IP=%%i"
    goto next
)
:next

:: 去除IP地址前后的空格
set ip=ipconfig | findstr /r"Address.*[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*"

:: 打印IP地址
echo IP Address: %IP%
echo 当前设备的IP是：%IP%
echo 这是你想要作为管理机的IP吗？
echo 注意：你必须将管理机的IP固定！你可以访问路由器配置实现设置本设备IP固定.
echo [1]是的，这是管理员机的IP [2]不，这不是管理员机
set /p "userInput=输入选项中的数字，然后按回车继续"
if /i "%userInput%"=="1" (
    set JSON_CONTENT=%JSON_TEMPLATE:*%IP%=%
) else (
    set userInput="NULL"
    set /p "userInput=输入，然后按回车继续"
)
pause

set JSON_CONTENT=%JSON_TEMPLATE:*%IP%=%


echo 请确认是否要执行后续操作（输入'yes'继续）：
pause


if /i "%errorlevel%"=="1" (
    rem 用户输入了'yes'，创建并保存JSON文件

) else (
    echo 操作已取消。
)

pause
