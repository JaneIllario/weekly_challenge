#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <filesystem>

namespace fs=std::filesystem;

int main(){

	std::string path="/src_txt"
	for (auto&p: fs::directory_iterator(path))
		std::cout<< p << std::endl;
}