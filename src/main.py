from PIL import Image, ImageDraw, ImageFont
import datetime

def create_image():
    img = Image.new('RGB', (800, 600), color=(73, 109, 137))
    d = ImageDraw.Draw(img)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    font = ImageFont.load_default()
    text = f"Current time is: {current_time}"
    d.text((10, 10), text, fill=(255, 255, 0), font=font)

    img.save('image.jpg')

if __name__ == "__main__":
    create_image()
