; �йش��� Inno Setup �ű��ļ�����ϸ��������İ����ĵ���

#define MyAppName "HephaestusOS USB ��װ����"
#define MyAppVersion "0.16 Alpha"
#define MyAppPublisher "ʷ�ٷ�ZMT SteveZMTstudios"
#define MyAppURL "https://github.com/SteveZMTstudios/Hephaestus"
#define MyAppExeName "usb_install_entry.exe"

[Setup]
; ע: AppId��ֵΪ������ʶ��Ӧ�ó���
; ��ҪΪ������װ����ʹ����ͬ��AppIdֵ��
; (��Ҫ�����µ� GUID�����ڲ˵��е�� "����|���� GUID"��)
AppId={{4A54CAA7-C53D-47BA-B9A2-1871716E99EE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\HephaestusOS USBinstaller
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=D:\git\Hephaestus\installer\Admin\LICENSE.txt
; ������ȡ��ע�ͣ����ڷǹ���װģʽ�����У���Ϊ��ǰ�û���װ����
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=D:\
OutputBaseFilename=usbinstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name:"cn";MessagesFile:"compiler:Languages\ChineseSimplified.isl"
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"
Name: "english"; MessagesFile: "compiler:Languages\English.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Hephaestus\installer\Admin\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\create_usb_image.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\create_usb_image.spec"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\save_config.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\usb_install_entry.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\ventoy-1.0.97-windows.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\source\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Hephaestus\installer\Admin\generate_config_json.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\output.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Hephaestus\installer\Admin\remove_usb_installer.py"; DestDir: "{app}"; Flags: ignoreversion
; ע��: ��Ҫ���κι���ϵͳ�ļ���ʹ�á�Flags: ignoreversion��

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

