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
	cout << "�̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡�" << endl;
	cout << "��   Hephaestus OS USB installer ��" << endl;
	cout << "��          USB ��װ����         ��" << endl;
	cout << "�̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡̡�" << endl;
	while (1) {
		cout << "[1]��װHephaestus OS ��USB�豸��\n[2]��USB�豸���Ƴ�Hephaestus OS\n\n���¶�Ӧ��������ִ�С�\n>";
	}
	string pythonPath = "python"; // ����Python��װ��ϵͳPATH��
	string insScriptPath = "create_usb_image.py";
	string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG";
	string command = pythonPath + " " + insScriptPath + " " + insScriptToken;

	int result = system(command.c_str());
	if (result == 0) {
		cout << "��������create_usb_image.py..." << endl;
	} else {
		cout << "Python����δ��⵽�����Ȱ�װPython��" << endl;
		cout << "�����Է��� https://www.python.org/downloads/ �����ذ�װ��" << endl;
		system("start https://www.python.org/downloads/");
		system("pause");
	}

	return 0;
}

