; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

#define MyAppName "Hephaestus OS USB 配置程序"
#define MyAppVersion "1.4 Beta 47117"
#define MyAppPublisher "史蒂夫ZMT SteveZMTstudios"
#define MyAppURL "https://github.com/SteveZMTstudios/Hephaestus"
#define MyAppExeName "usb_install_entry.exe"

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (若要生成新的 GUID，可在菜单中点击 "工具|生成 GUID"。)
AppId={{E927F3C5-633B-492B-AA43-4BD62E5D2EB3}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=D:\HephaestusOS\Admin\USB_installer
DisableDirPage=yes
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=D:\Hephaestus\installer\Admin\LICENSE.txt
InfoBeforeFile=D:\Hephaestus\installer\Admin\notice_before_usb_inst.txt
; 以下行取消注释，以在非管理安装模式下运行（仅为当前用户安装）。
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=commandline
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"
Name: "english"; MessagesFile: "compiler:Languages\English.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Hephaestus\installer\Admin\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\create_usb_image.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\remove_usb_installer.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\usb_install_entry.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\ventoy-1.0.97-windows.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\source\*"; DestDir: "{app}\source"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\source\Lang\*"; DestDir: "{app}\source\Lang"; Flags: ignoreversion recursesubdirs createallsubdirs
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

