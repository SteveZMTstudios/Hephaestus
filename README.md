**简体中文** | [English (US)](https://stevezmtstudios.github.io/Hephaestus/README_EN)

# Hephaestus 赫菲斯托斯
A tool that make repairing school teaching computer easier.
一个使维护学校教学计算机更容易的工具。

![build status](https://img.shields.io/badge/Build-Public_Archive-yellow?style=flat&logo=Github&logoColor=white&label=build&labelColor=grey)
![platform](https://img.shields.io/badge/platform-Windows-blue?style=flat&logoColor=white&label=platform&labelColor=grey)
![Static Badge](https://img.shields.io/badge/compile_status-Public_Archive-red?style=flat&logoColor=white&label=compile&labelColor=grey)

# Stop Update Notice 停止更新公示
> Οι θεοί έχουν ολοκληρωθούν. <br>
> Dei sunt cecideri. <br>
> The gods have fallen.

[查看详情](https://www.coolapk.com/feed/55461349?shareKey=NTg5NzdlYzgwNmI1NjYzYzkwMTA~&shareUid=22536770&shareFrom=com.coolapk.market_14.1.1)



# Install 安装
![Static Badge](https://img.shields.io/badge/Get_release-Here!-yellow?style=flat&logo=download&logoColor=white&labelColor=grey&link=https%3A%2F%2Fgithub.com%2FSteveZMTstudios%2FHephaestus%2Freleases)


[usb安装器-Release](https://github.com/SteveZMTstudios/Hephaestus/releases)
<br>联机安装包需要确保网络环境畅通。可能会不稳定。离线安装包可以在任何环境下运行，推荐使用离线安装包。
<br>需要帮助? 访问[wiki 页面](https://github.com/SteveZMTstudios/Hephaestus/wiki)



# Build 构建
本程序采用源代码构建，因此您不需要编译python文件。

# How the idea is implemented 实现思路
~~通过使用一个集中的安装包（由管理系统生成）安装到各个教室的计算机上，同时创建一个配套的ISO镜像实现未加入配置组的计算机能够临时地，方便的获取到内网存储的系统安装映像；集中安装包可以创建一个开机启动项，当操作系统损坏为轻度时，重启到镜像只给管理员发送电子邮件并自动将部署在学校内网服务器上的iso下载下来，当下载完成时弹出友好加载框或使用tinytask实现无操作自动进入普通的windows修复；当操作系统重度损坏以至于只能启动到pe时，winpe会部署一个可以临时使用的环境，可供教师使用基本的PPT放映功能，word和excel编辑，白板和展台功能；同时安装程序会在后台自动运行windows安装程序并发送电子邮件；当Windows重装完成后会弹出一个窗口告知教师和电教委员，当计算机处于空闲状态时便可以重新启动。~~
<br>~~安装给教室的ISO映像可以是定制的，预装一些必要的文件（如office，希沃教学套件等），也可以在配置系统时由管理员定制。~~

~~安装在各台电脑的安装包只实现几个功能：通过获取已经写在安装包里面的URL获取WinPE和定制Windows安装镜像链接和管理员电邮，它们将被储存到C:\Windows\Hephaestus文件夹中，同时注册系统启动项。~~

管理员的安装包需要做的：
~~1. 本地配置服务器或者使用已有的一个内网服务器用作CDN分发url，因此要做好ip固定~~
~~2. 将服务器脚本设置为开机自启，这可能会拖慢开机速度，所以建议直接使用学校内配置NAS的服务器；~~
~~3. 填写管理员的电邮地址~~
~~4. 自定义Windows安装程序的预装程序~~
~~5. 配置winpe的工作方式，包括是否允许在万不得已的时候格式化全盘并重新安装操作系统~~
6. 制作~~教室电脑安装包和~~启动u盘
~~7. 收集各个班winpe的启动情况，如有集中启动则电邮报告管理员可能存在恶性病毒传播或者Windows安装了一个异常的更新。~~
<br>*因为开发周期有限，现在这个程序只开发了usb安装程序和WinPE内核映像以及集成了必要的驱动和可选的软件。如果有时间我会补完这个项目。*


# The source of the idea 为什么这么做
23年11月，我们学校教室的希沃一体机出现了大量的死机和不开机问题，当时网管真忙不过来，于是部分班主任求助于S同学和我。这一过程非常的无聊和繁琐，并且耽误上课进度，部分班因为使用希沃自带恢复操作系统工具而导致了严重的教学事故，故计划编写此程序。

# Contributions 参考的来源
WinPE镜像：[**此作品修改自Edgeless Powered by Cnotech**](https://home.edgeless.top/) <-点击访问原始项目的主页

