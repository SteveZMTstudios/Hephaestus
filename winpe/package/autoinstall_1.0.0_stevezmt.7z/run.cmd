setlocal
echo msgbox "内置系统未能正确加载或者无法启动，已经临时启动此虚拟化系统。",64,"Hephaestus Notice">welcome.vbs && start welcome.vbs && ping -n 2 127.1>nul && del welcome.vbs

setlocal

:: 设置当前目录为脚本所在目录
cd /d "%~dp0"

:: 读取config.json文件并提取system_img_url字段的值
for /f "tokens=1,* delims=:" %%a in ('findstr "system_img_url" config.json') do (
    set "url=%%b"
)

set "url=%url:"=%"

if not defined url (
    exit /b
)

:: 使用curl下载文件到C盘根目录
curl -L "%url%" -o C:\system_image.img

echo msgbox "系统恢复镜像已经下载完毕。",64,"Hephaestus Notice">download_complete.vbs && start download_complete.vbs && ping -n 2 127.1>nul && del download_complete.vbs
X:\Program Files\Edgeless\

endlocal

