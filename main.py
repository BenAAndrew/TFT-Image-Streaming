import argparse
from serial import Serial
from PIL import Image
from time import sleep

BAUDRATE = 19200
TIMEOUT = 0.1


def send_image(serial, image_path, width, height, max_colours):
    # Preprocess image
    img = Image.open(image_path).resize((width, height), Image.ANTIALIAS)
    img = img.quantize(max_colours).convert("RGB")

    # Read image colours into (R,G,B) tuples
    pixels = [img.getpixel((i, j)) for i in range(width) for j in range(height)]

    # Send colours
    colours = list(set(pixels))
    serial.write(bytes([len(colours)]))
    for colour in colours:
        serial.write(bytes(colour))

    # Send pixel colour indexes
    for pixel in pixels:
        serial.write(bytes([colours.index(pixel)]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stream image to arduino TFT screen")
    parser.add_argument("-p", "--com_port", type=str, help="Arduino COM port (i.e. COM3)", required=True)
    parser.add_argument("-i", "--image_path", type=str, help="Image path", default="test.png")
    parser.add_argument("-w", "--width", type=int, help="Screen width (pixels)", default=128)
    parser.add_argument("-z", "--height", type=int, help="Screen height (pixels)", default=160)
    parser.add_argument("-c", "--colours", type=int, help="Maximum colours", default=100)
    args = parser.parse_args()

    # Connect to arduino
    arduino = Serial(args.com_port, BAUDRATE, timeout=TIMEOUT)
    sleep(5)

    # Send image
    send_image(arduino, args.image_path, args.width, args.height, args.colours)

    # Display until key press
    input("Press any key to stop...")
