#include <iostream>
#include <cstdlib>
#include <string>
#include <csignal>
#include <windows.h>
#include <stdlib.h>
using namespace std;

int main() {
	int result;
	result = system("python aefi.py");
	cout << result;
	return 0;
}