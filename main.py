import cv2
import os
from PIL import Image

# ASCII 字元（由深至淺）
ASCII_CHARS = "@%#*+=-:. "

#=====像素to字元=======
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # 調整文字比例
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # 轉灰階

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(
        ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))] for pixel in pixels
    )
    return ascii_str

def image_to_ascii(path, width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"❌ 無法開啟圖片 {path}: {e}")
        return ""

    image = resize_image(image, width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    
    lines = [ascii_str[i:i+width] for i in range(0, pixel_count, width)]
    ascii_image = "\n".join(line if line.strip() else "" for line in lines)
    return ascii_image
#=============================

#=====切偵========
def extract_frames(video_path, output_dir="frames", max_frames=None, fps_skip=1):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ 無法讀取影片！")
        return 0

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"🎞️ 影片總幀數：{total_frames}")

    count = 0
    saved = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        if count % fps_skip == 0:
            frame_path = os.path.join(output_dir, f"frame_{saved:04d}.png")
            cv2.imwrite(frame_path, frame)
            saved += 1

            if max_frames and saved >= max_frames:
                break

        count += 1

    cap.release()
    print(f"✅ 已擷取 {saved} 幀圖片到資料夾：{output_dir}")
    return saved
#===========
#=====store========
def generate_ascii_animation(video_path, output_txt="ascii_animation.txt", frame_width=100, fps_skip=1, max_frames=None):
    temp_dir = "ascii_frames"
    total = extract_frames(video_path, output_dir=temp_dir, max_frames=max_frames, fps_skip=fps_skip)

    with open(output_txt, "w", encoding="utf-8") as out:
        for i in range(total):
            frame_file = os.path.join(temp_dir, f"frame_{i:04d}.png")
            ascii_art = image_to_ascii(frame_file, width=frame_width)
            out.write(ascii_art)
            out.write("\n===FRAME===\n")

    print(f"✅ ASCII 動畫儲存完成：{output_txt}")
#====================

# ✅ 使用方式
if __name__ == "__main__":
    generate_ascii_animation(
        video_path="bad_apple.mp4",  # ← 替換成你的影片
        output_txt="ascii_animation.txt",
        frame_width=240,
        fps_skip=1,       # 每2幀擷取一次（加快轉換速度）
        max_frames=None    # 最多100幀（None = 全部）
    )

