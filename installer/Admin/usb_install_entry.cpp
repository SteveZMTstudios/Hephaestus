#include <iostream>
#include <cstdlib>
#include <string>
#include <windows.h>

int main() {
    std::string pythonPath = "python"; // ����Python��װ��ϵͳPATH��
    std::string insScriptPath = "create_usb_image.py";
    std::string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG"
    std::string command = pythonPath + " " + insScriptPath + " " + insScriptToken;
    
    int result = std::system(command.c_str());
    if (result == 0) {
        std::cout << "��������create_usb_image.py..." << std::endl;
    } else {
        std::cout << "Python����δ��⵽�����Ȱ�װPython��" << std::endl;
        std::cout << "�����Է��� https://www.python.org/downloads/ �����ذ�װ��" << std::endl;
        std::system("start https://www.python.org/downloads/")
    }

    return 0;
}

