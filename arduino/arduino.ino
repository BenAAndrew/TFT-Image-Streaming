#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
#include <SPI.h>

// TFT Screen
#define sclk 13
#define mosi 12
#define cs   11
#define dc   10
#define rst  9

#define width 128
#define height 160
Adafruit_ST7735 tft = Adafruit_ST7735(cs, dc, mosi, sclk, rst);

// Variables
uint8_t num_colours;
uint8_t index;
uint8_t r;
uint8_t g;
uint8_t b;

void setup() {
  tft.initR(INITR_BLACKTAB);
  tft.fillScreen(ST7735_BLACK);
  Serial.begin(19200);
}

void loop() {
  // Colours
  num_colours = getNextInput();
  int colours[num_colours];
  for(uint8_t i = 0; i < num_colours; i++){
    r = getNextInput();
    g = getNextInput();
    b = getNextInput();
    colours[i] = tft.Color565(r,g,b);
  }

  // Drawing
  for(uint8_t x = 0; x < width; x++){
    for(uint8_t y = 0; y < height; y++){
      index = getNextInput();
      tft.drawPixel(x, y, colours[index]);
    }
  }
}

uint8_t getNextInput() {
  while(!Serial.available());
  return Serial.read();
}
