#include <FastLED.h>
#include <ArduinoJson.h>
#include <EEPROM.h>

// {"r":10,"g":30,"b":40}

DynamicJsonDocument doc(1024);

#define NUM_LEDS 1
#define DATA_PIN 2
#define CLOCK_PIN 3
#define BRIGHTNESS  250

CRGB leds[NUM_LEDS];

#define UPDATES_PER_SECOND 200

CRGBPalette16 currentPalette;
TBlendType    currentBlending;

extern CRGBPalette16 myRedWhiteBluePalette;
extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;

int integerFromPC = 0;

void setRGB(int red, int green, int blue) {
    leds[0].red   = red;
    leds[0].green = green;
    leds[0].blue  = blue;
    FastLED.show();
}

void setup() {
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
    bool dataChanged = false;

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
    if (dataChanged) {
        status();
    }

    FastLED.show();
    FastLED.delay(1000 / UPDATES_PER_SECOND);
}

void status() {
    Serial.println(String(leds[0].red) + "," + String(leds[0].green) + "," + String(leds[0].blue) + "," + String(FastLED.getBrightness()));
}
