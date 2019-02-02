#include <FastLED.h>
#include <ArduinoJson.h>
#include <EEPROM.h>

DynamicJsonDocument doc(1024);

#define NUM_LEDS 1
#define DATA_PIN 2
#define CLOCK_PIN 3

CRGB leds[NUM_LEDS];

#define UPDATES_PER_SECOND 200

CRGBPalette16 currentPalette;
TBlendType    currentBlending;

extern CRGBPalette16 myRedWhiteBluePalette;
extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;

void setRGB(int red, int green, int blue) {
    leds[0].red   = red;
    leds[0].green = green;
    leds[0].blue  = blue;
    FastLED.show();
}

void setup() {
    if (!(EEPROM.read(4) == 0 || EEPROM.read(4) == 1)) {
        EEPROM.write(4, 1);
    }

    FastLED.addLeds<P9813, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );

    Serial.begin(115200);

    setRGB(255,0,0);
    delay(200);
    setRGB(0,255,0);
    delay(200);
    setRGB(0,0,255);
    delay(200);
    reset();

    Serial.println("READY");
    status();
}

void reset() {
    setRGB(EEPROM.read(0), EEPROM.read(1), EEPROM.read(2));
    FastLED.setBrightness(EEPROM.read(3));
    FastLED.show();
}

void loop()
{
    String input = Serial.readStringUntil('\n');
    deserializeJson(doc, input);
    JsonObject obj = doc.as<JsonObject>();
    String r = obj["r"];
    String g = obj["g"];
    String b = obj["b"];
    String br = obj["br"];
    String onoff = obj["onoff"];
    bool dataChanged = false;

    if (onoff != "null") {
        dataChanged = true;
        EEPROM.write(4, onoff.toInt() == 1 ? 1 : 0);
    }

    if (EEPROM.read(4) == 1) {
        if (r != "null") {
            leds[0].red   = r.toInt();
            dataChanged = true;
            EEPROM.write(0, leds[0].red);
        }
        if (g != "null") {
            leds[0].green = g.toInt();
            dataChanged = true;
            EEPROM.write(1, leds[0].green);
        }
        if (b != "null") {
            leds[0].blue  = b.toInt();
            dataChanged = true;
            EEPROM.write(2, leds[0].blue);
        }
        if (br != "null") {
            FastLED.setBrightness(br.toInt());
            dataChanged = true;
            EEPROM.write(3, br.toInt());
        }
        reset();
    } else {
        FastLED.setBrightness(0);
        setRGB(0,0,0);
    }
    if (dataChanged) {
        status();
    }
    FastLED.delay(1000 / UPDATES_PER_SECOND);
}

void status() {
    Serial.println(String(leds[0].red) + "," + String(leds[0].green) + "," + String(leds[0].blue) + "," + String(FastLED.getBrightness()) + "," + String(EEPROM.read(4)));
}
