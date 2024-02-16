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

:: ȥ��IP��ַǰ��Ŀո�
set ip=ipconfig | findstr /r"Address.*[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*"

:: ��ӡIP��ַ
echo IP Address: %IP%
echo ��ǰ�豸��IP�ǣ�%IP%
echo ��������Ҫ��Ϊ�������IP��
echo ע�⣺����뽫�������IP�̶�������Է���·��������ʵ�����ñ��豸IP�̶�.
echo [1]�ǵģ����ǹ���Ա����IP [2]�����ⲻ�ǹ���Ա��
set /p "userInput=����ѡ���е����֣�Ȼ�󰴻س�����"
if /i "%userInput%"=="1" (
    set JSON_CONTENT=%JSON_TEMPLATE:*%IP%=%
) else (
    set userInput="NULL"
    set /p "userInput=���룬Ȼ�󰴻س�����"
)
pause

set JSON_CONTENT=%JSON_TEMPLATE:*%IP%=%


echo ��ȷ���Ƿ�Ҫִ�к�������������'yes'��������
pause


if /i "%errorlevel%"=="1" (
    rem �û�������'yes'������������JSON�ļ�

) else (
    echo ������ȡ����
)

pause
