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
	atexit(defaultExit);
	signal(SIGINT, signalHandler);
	system("rmdir /s /q .\\program");
	cout << "√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√" << endl;
	cout << "√   Hephaestus OS USB installer √" << endl;
	cout << "√          USB 安装程序         √" << endl;
	cout << "√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√" << endl;
	while (1) {
		cout << "[1]安装Hephaestus OS 到USB设备。\n[2]从USB设备上移除Hephaestus OS\n\n按下对应的数字来执行。\n>";
	}
	string pythonPath = "python"; // 假设Python安装在系统PATH中
	string insScriptPath = "create_usb_image.py";
	string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG";
	string command = pythonPath + " " + insScriptPath + " " + insScriptToken;

	int result = system(command.c_str());
	if (result == 0) {
		cout << "正在运行create_usb_image.py..." << endl;
	} else {
		cout << "Python环境未检测到，请先安装Python。" << endl;
		cout << "您可以访问 https://www.python.org/downloads/ 来下载安装。" << endl;
		system("start https://www.python.org/downloads/");
		system("pause");
	}

	return 0;
}

