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
	cout << "���ڰ�װ���������Ե�...\n";
	int result = system("pip install colorama -i https://pypi.tuna.tsinghua.edu.cn/simple");//install extra package
	if (result == 1)  {
		cout << "Python����δ��⵽�����Ȱ�װPython��" << endl;
		cout << "�����Է��� https://www.python.org/downloads/ �����ذ�װ��" << endl;
		system("start https://www.python.org/downloads/");
		system("pause");
		done = 1;
		return 0;
	}
	cout << "�̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡�" << endl;
	cout << "��   Hephaestus OS USB installer ��" << endl;
	cout << "��          USB ��װ����         ��" << endl;
	cout << "�̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡�" << endl;
	while (1) {
		cout << "[1]��װHephaestus OS ��USB�豸��\n[2]��USB�豸���Ƴ�Hephaestus OS\n\n���¶�Ӧ��������ִ�С�\n>";
		cin >> result;
		string pythonPath = "python"; // ����Python��װ��ϵͳPATH��
		string insScriptPath = "create_usb_image.py";
		string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG";
		string remScriptPath = "remove_usb_installer.py";
		string remScriptToken = "djlQok91BTI4D6F2pAt87IJFmsMxTXcy";


		if (result == 0) {
			if (select == 1) {

				cout << "��������create_usb_image.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + insScriptPath + " " + insScriptToken;
				system(command.c_str());
				done = 1;
			} else if (select == 2) {
				cout << "��������remove_usb_image.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + remScriptPath + " " + remScriptToken;
				system(command.c_str());
				done = 1;
			} else {
				cout << "���벻�Ϸ��������ԡ�" << endl;
			}

		} else if (result == 1)  {
			cout << "Python����δ��⵽�����Ȱ�װPython��" << endl;
			cout << "�����Է��� https://www.python.org/downloads/ �����ذ�װ��" << endl;
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

