#include <iostream>
#include <cstdlib>
#include <string>
#include <csignal>
#include <windows.h>
#include <stdlib.h>
using namespace std;

void defaultExit(void) {
	system("rmdir /s /q .\\program");
}

void signalHandler( int signum = 0 ) {
	cout << "Interrupt signal (" << signum << ") received.\n";
	system("rmdir /s /q .\\program");
	system("pause");
	exit(signum);
}

int main() {
	int select = 0, done = 0;
	atexit(defaultExit);
	signal(SIGINT, signalHandler);
	system("rmdir /s /q .\\program");
	system("cls");
	system("color 9f");
	cout << "正在安装环境，请稍等...\n";
	int result = system("pip install colorama -i https://pypi.tuna.tsinghua.edu.cn/simple");//install extra package
	if (result == 1)  {
		cout << "Python环境未检测到，请先安装Python。" << endl;
		cout << "您可以访问 https://www.python.org/downloads/ 来下载安装。" << endl;
		system("start https://www.python.org/downloads/");
		system("pause");
		done = 1;
		return 0;
	}
	cout << "√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√" << endl;
	cout << "√   Hephaestus OS USB installer √" << endl;
	cout << "√          USB 安装程序         √" << endl;
	cout << "√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√" << endl;
	while (1) {
		cout << "[1]安装Hephaestus OS 到USB设备。\n[2]从USB设备上移除Hephaestus OS\n\n按下对应的数字来执行。\n>";
		cin >> result;
		string pythonPath = "python"; // 假设Python安装在系统PATH中
		string insScriptPath = "create_usb_image.py";
		string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG";
		string remScriptPath = "remove_usb_installer.py";
		string remScriptToken = "djlQok91BTI4D6F2pAt87IJFmsMxTXcy";


		if (result == 0) {
			if (select == 1) {

				cout << "正在运行create_usb_image.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + insScriptPath + " " + insScriptToken;
				system(command.c_str());
				done = 1;
			} else if (select == 2) {
				cout << "正在运行remove_usb_image.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + remScriptPath + " " + remScriptToken;
				system(command.c_str());
				done = 1;
			} else {
				cout << "输入不合法，请重试。" << endl;
			}

		} else if (result == 1)  {
			cout << "Python环境未检测到，请先安装Python。" << endl;
			cout << "您可以访问 https://www.python.org/downloads/ 来下载安装。" << endl;
			system("start https://www.python.org/downloads/");
			system("pause");
			done = 1;
		}
		if (done == 1) {
			return 0;
		}
	}
	return 0;
}

