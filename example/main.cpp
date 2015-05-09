#include <Arduino.h>

#define PIN 13

void setup() {

    pinMode(PIN, OUTPUT);

}


void loop() {

    digitalWrite(PIN, LOW);
    delay(600);

    digitalWrite(PIN, HIGH);
    delay(600);
}