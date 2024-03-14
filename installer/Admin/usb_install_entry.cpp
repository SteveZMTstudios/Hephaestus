#include <iostream>
#include <cstdlib>
#include <string>
#include <csignal>
#include <windows.h>
#include <stdlib.h>
#include <locale.h>

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
	cout << "Installing environment, Please wait for a sec...\n";

	int result = system("pip install colorama requests tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple");//install extra package
	/*
	if (result == 1 )  {
		cout << "Python environment wasn not detected, Please Install Python 3+ First! " << endl;
		cout << "Visit https://www.python.org/downloads/ to download and install." << endl;
		system("start https://www.python.org/downloads/");
		system("pause");
		done = 1;
		return 0;
	}
	*/
	system("cls");
	
	cout << "============================" << endl;
	cout << " Hephaestus OS USB installer " << endl;
	cout << "============================" << endl;
	cout << endl;
	while (1) {
		cout << "[1]Install \n[2]Remove\n>";
		cin >> select;
		string pythonPath = "python";
		string insScriptPath = "create_usb_image.py";
		string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG";
		string remScriptPath = "remove_usb_installer.py";
		string remScriptToken = "djlQok91BTI4D6F2pAt87IJFmsMxTXcy";


		if (result == 0) {
			if (select == 1) {

				cout << "Running create_usb_image.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + insScriptPath + " " + insScriptToken;
				
				result = system(command.c_str());
				done = 1;
			} else if (select == 2) {
				cout << "Running remove_usb_installer.py..." << endl;
				system("color 0f");
				string command = pythonPath + " " + remScriptPath + " " + remScriptToken;
				result = system(command.c_str());
				done = 1;
			} else {
				cout << "Invalid input, Please Try again." << endl;
			}

		} else if (result == 1)  {
			cout << "Python environment wasn not detected, Please Install Python 3+ First! " << endl;
			cout << "Visit https://www.python.org/downloads/ to download and install." << endl;
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

