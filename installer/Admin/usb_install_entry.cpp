#include <iostream>
#include <cstdlib>
#include <string>

int main() {
    std::string pythonPath = "python"; // ����Python��װ��ϵͳPATH��
    std::string scriptPath = "create_usb_image.py";
    std::string command = pythonPath + " " + scriptPath;
    int result = std::system(command.c_str());
    if (result == 0) {
        std::cout << "��������create_usb_image.py..." << std::endl;
    } else {
        std::cout << "Python����δ��⵽�����Ȱ�װPython��" << std::endl;
        std::cout << "�����Է��� https://www.python.org/downloads/ �����ذ�װ��" << std::endl;
    }

    return 0;
}

