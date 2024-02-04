@echo off
setlocal EnableDelayedExpansion

:: 初始化变量
set config_url=
set system_img_url=
set is_allow_formatall=
set ext_url=

echo 请输入配置文件的获取路径URL:
set /p config_url=

echo 请输入系统镜像的获取路径:
set /p system_img_url=

echo 请确认是否允许重装时格式化C盘，输入true或false:
set /p is_allow_formatall=

echo 请输入扩展包（将在重置后预先安装到系统）的获取路径:
set /p ext_url=


:: 构建JSON字符串，确保属性值被双引号包围
set json={
set json=!json!"config_url":"%config_url%"
set json=!json!,"system_img_url":"%system_img_url%"
set json=!json!,"is_allow_formatall":%is_allow_formatall%
set json=!json!,"ext_url":"%ext_url%"
set json=!json!

:: 补上缺失的右括号
set json=!json!}

:: 输出JSON字符串，并确保使用正确的双引号
echo !json!

:: 如果需要保存到文件，可以使用以下命令：
echo !json! > .\output.json

endlocal





