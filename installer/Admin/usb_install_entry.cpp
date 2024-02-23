#include <iostream>
#include <cstdlib>
#include <string>
#include <windows.h>

int main() {
    std::string pythonPath = "python"; // 假设Python安装在系统PATH中
    std::string insScriptPath = "create_usb_image.py";
    std::string insScriptToken = "C1eJrHgEQMzy6hlWOhrkhAYkJfP9QJrG"
    std::string command = pythonPath + " " + insScriptPath + " " + insScriptToken;
    
    int result = std::system(command.c_str());
    if (result == 0) {
        std::cout << "正在运行create_usb_image.py..." << std::endl;
    } else {
        std::cout << "Python环境未检测到，请先安装Python。" << std::endl;
        std::cout << "您可以访问 https://www.python.org/downloads/ 来下载安装。" << std::endl;
        std::system("start https://www.python.org/downloads/")
    }

    return 0;
}

