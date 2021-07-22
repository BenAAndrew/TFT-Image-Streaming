# TFT-Image-Streaming
Stream images to an Arduino TFT screen **without an SD card**.

## Setup
1. Install [Python](https://www.python.org/)
2. Run `pip install -r requirements.txt`
3. Copy the folders in `libraries` into your arduino libraries folder (typically `Documents\Arduino\libraries`)
4. Upload the `arduino/arduino.ino` sketch to your arduino
5. Ensure the pins defined in the sketch (lines 6-10) match your wiring

## Usage
`main.py` supports a range of arguments:
- **com_port**: The COM port of your arduino (i.e. COM3)
- **image_path**: Path to the image you want to display (Defaults to test.png)
- **width**: The width of your screen in pixels (Default is 128)
- **height**: The height of your screen in pixels (Default is 160)
- **colours**: The maximum number of colours (used for compression. Default is 100)

Example: `python main.py --com_port COM3 --image_path dog.png` sends the image 'dog.png' to the arduino on port COM3.

## Using other displays
The arduino code is currently specific to a Adafruit_ST7735 compatible 128x160 display.

To change displays, change the pins, width & height (defined from lines 6-13) to those of your display.

You may also need to change the Adafruit_ST7735 library to another display library.
