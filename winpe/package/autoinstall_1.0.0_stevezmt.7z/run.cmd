setlocal
echo msgbox "����ϵͳδ����ȷ���ػ����޷��������Ѿ���ʱ���������⻯ϵͳ��",64,"Hephaestus Notice">welcome.vbs && start welcome.vbs && ping -n 2 127.1>nul && del welcome.vbs

setlocal

:: ���õ�ǰĿ¼Ϊ�ű�����Ŀ¼
cd /d "%~dp0"

:: ��ȡconfig.json�ļ�����ȡsystem_img_url�ֶε�ֵ
for /f "tokens=1,* delims=:" %%a in ('findstr "system_img_url" config.json') do (
    set "url=%%b"
)

set "url=%url:"=%"

if not defined url (
    exit /b
)

:: ʹ��curl�����ļ���C�̸�Ŀ¼
curl -L "%url%" -o C:\system_image.img

echo msgbox "ϵͳ�ָ������Ѿ�������ϡ�",64,"Hephaestus Notice">download_complete.vbs && start download_complete.vbs && ping -n 2 127.1>nul && del download_complete.vbs
X:\Program Files\Edgeless\

endlocal

