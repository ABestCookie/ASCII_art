from PIL import Image

# ASCII 字元（由深至淺）
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # 調整文字比例
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # 轉灰階

def pixels_to_ascii(image):
    pixels = image.getdata()
    # 修正：將像素值正確映射到 ASCII_CHARS 索引範圍
    ascii_str = "".join(
        ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))] for pixel in pixels
    )
    return ascii_str

def image_to_ascii(path, width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        print("無法開啟圖片:", e)
        return

    image = resize_image(image, width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:i+width] for i in range(0, pixel_count, width))
    return ascii_image

# 使用範例
ascii_art = image_to_ascii("fanart.jpg", width=800)
if ascii_art:
    with open("output.txt", "w") as f:
        f.write(ascii_art)
else:
    print("ASCII 藝術產生失敗。")
