@echo off
setlocal EnableDelayedExpansion

:: ��ʼ������
set config_url=
set system_img_url=
set is_allow_formatall=
set ext_url=

echo �����������ļ��Ļ�ȡ·��URL:
set /p config_url=

echo ������ϵͳ����Ļ�ȡ·��:
set /p system_img_url=

echo ��ȷ���Ƿ�������װʱ��ʽ��C�̣�����true��false:
set /p is_allow_formatall=

echo ��������չ�����������ú�Ԥ�Ȱ�װ��ϵͳ���Ļ�ȡ·��:
set /p ext_url=


:: ����JSON�ַ�����ȷ������ֵ��˫���Ű�Χ
set json={
set json=!json!"config_url":"%config_url%"
set json=!json!,"system_img_url":"%system_img_url%"
set json=!json!,"is_allow_formatall":%is_allow_formatall%
set json=!json!,"ext_url":"%ext_url%"
set json=!json!

:: ����ȱʧ��������
set json=!json!}

:: ���JSON�ַ�������ȷ��ʹ����ȷ��˫����
echo !json!

:: �����Ҫ���浽�ļ�������ʹ���������
echo !json! > .\output.json

endlocal





