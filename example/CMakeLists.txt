# Le asignamos el nombre a nuestro proyecto
set(PROJECT_NAME Blink)


# Generamos el Firmware
generate_arduino_firmware(${PROJECT_NAME}
    SRCS main.cpp
    PORT /dev/ttyACM0
    BOARD micro
    ARDLIBS SoftwareSerial
)


