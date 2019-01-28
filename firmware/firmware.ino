#include <FastLED.h>
#include <ArduinoJson.h>

// {"r":10,"g":30,"b":40}

DynamicJsonDocument doc;

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

void setup() {
    FastLED.addLeds<P9813, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );

    Serial.begin(115200);

    reset();
    delay(100);
    leds[0].red   = 255;
    FastLED.show();
    delay(100);
    leds[0].green = 255;
    FastLED.show();
    delay(100);
    leds[0].blue  = 255;
    FastLED.show();
    delay(100);
    reset();

    Serial.println("READY");
    status();
}

void reset() {
    leds[0].red   = 0;
    leds[0].green = 0;
    leds[0].blue  = 0;
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
    }
    if (g != "null") {
        leds[0].green = g.toInt();
        dataChanged = true;
    }
    if (b != "null") {
        leds[0].blue  = b.toInt();
        dataChanged = true;
    }
    if (br != "null") {
        FastLED.setBrightness(br.toInt());
        dataChanged = true;
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
