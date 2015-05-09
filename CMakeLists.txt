set(CMAKE_TOOLCHAIN_FILE cmake/ArduinoToolchain.cmake)
cmake_minimum_required(VERSION 3.0)

project(Blink C CXX)

print_board_list()
print_programmer_list()

## Especificar la carpeta dónde tienes las librerías
link_directories(${ARDUINO_SDK}/libraries)

#Añadimos la carpeta de nuestro código
add_subdirectory(example)
