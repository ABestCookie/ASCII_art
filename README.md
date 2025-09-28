# ASCII_art
> 拿來玩bad apple的地方

眾所周知bad apple的MV只要在可以被電訊號控制明暗的東西上都能被播放

---
這東西就是用來在終端小黑窗播放bad apple用的

<small>(當然你要拿來播其他東西也是可以的)</small>

## 原理

應該很容易理解吧，這東西不需要我多說

就是用cv2切偵+pillow轉灰階跟替換像素

## 食用方法

下載原始碼

然後修改一下 `main.py`裡面的這個部分

```python
if __name__ == "__main__":
    generate_ascii_animation(
        video_path="bad_apple.mp4",  # ← 替換成你的影片
        output_txt="ascii_animation.txt", #輸出檔案的位置(這邊是相對路徑，你也可以放絕對路徑)
        frame_width=240,    #生成字元畫的大小
        fps_skip=1,       # 每2幀擷取一次（加快轉換速度）
        max_frames=None    # 最多幾幀（None = 全部）
    )
```

> 如果需要從yt下載影片，我有放 `yt.py`，把裡面字串連結改成你要的連結就能用了
>
> 當然別忘記讓他跑起來
>
> ```
> python yt.py
> ```

然後配置一下你的環境

```batch
pip install -r requirements.txt
```

然後運行

**產生動畫**

```batch
python main.py
```
> 這邊在運行的時候，由於我沒做進度條，因此根據不同的電腦配置有可能會跑很久的時間

**播放動畫**

```batch
python play.py
```
> 你也可以運行 `play.exe` 不過動畫檔的名字需固定為 `ascii_animation.txt`


## Example flim

[【Bad Apple but in Windows Terminal】](https://youtu.be/YZyhZMwJDAI?si=T2VK5Nc789RzRzSz)

