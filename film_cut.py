import cv2
import os

def extract_frames(video_path, output_dir="frames", max_frames=None, fps_skip=1):
    """
    將影片拆成圖片幀。
    
    - video_path: 影片路徑
    - output_dir: 儲存幀的資料夾
    - max_frames: 最多幾幀 (None = 全部)
    - fps_skip: 每幾幀取一幀（1 = 全部，2 = 每秒取一幀）

    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ 無法讀取影片！")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"🎞️ 總幀數：{total_frames}")

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
    print(f"✅ 已儲存 {saved} 幀到資料夾：{output_dir}")

# ✅ 使用方式
extract_frames("bad_apple.mp4", output_dir="film_output", fps_skip=1)
