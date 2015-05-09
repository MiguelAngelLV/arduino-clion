# Le asignamos el nombre a nuestro proyecto
set(PROJECT_NAME Blink)

set(PORT /dev/ttyACM1)

# Generamos el Firmware
generate_arduino_firmware(${PROJECT_NAME}
    SRCS main.cpp
    PORT ${PORT}
    BOARD micro
    ARDLIBS SoftwareSerial)


#Descomentar estas líneas si tu placa necesita "reset".
#En algunas ocasiones requiere hacer el upload dos veces.

#add_custom_target(
#    ${PROJECT_NAME}-reset
#    ${PROJECT_SOURCE_DIR}/cmake/reset.py ${PORT}
#)
#
#add_dependencies(${PROJECT_NAME}-reset  ${PROJECT_NAME})
#add_dependencies(${PROJECT_NAME}-upload  ${PROJECT_NAME}-reset ${PROJECT_NAME})

