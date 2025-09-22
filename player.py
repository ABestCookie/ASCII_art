import os
import time

def load_frames_from_file(path, delimiter="===FRAME==="):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return [frame.strip() for frame in content.split(delimiter) if frame.strip()]

def play_animation(frames, delay=0.05):
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    for frame in frames:
        clear()
        print(frame)
        time.sleep(delay)

if __name__ == "__main__":
    ascii_file = "ascii_animation.txt"  # 改成你的 ASCII 動畫檔案路徑
    delay = 0.005                         # 每幀的延遲時間（秒）

    frames = load_frames_from_file(ascii_file)
    print(f"🎬 共載入 {len(frames)} 幀，開始播放...")
    time.sleep(1)

    play_animation(frames, delay=delay)
