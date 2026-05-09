import tkinter as tk 
import random 
import time 
import sys 
import math 

texts = [ 
    '好好吃饭，别饿着。', '顺顺利利，万事胜意。', '保持好心情，爱自己。', '天冷了多穿衣服。',
    '我想你了。', '别熬夜，早点睡。', '你是最棒的。', '照顾好自己。', '开心每一天。',
    '少喝冷饮，多喝温水。', '记得吃早餐。', '按时吃饭。', '加油，你是最棒的。',
    '别给自己太大的压力。', '累了就休息一下。', '记得多运动。', '多吃水果蔬菜。',
    '睡前喝杯温牛奶。', '别感冒了。', '开开心心，快快乐乐。', '你真的很重要。',
    '做一个快乐的人。', '不要忘记微笑。', '生活明朗，万物可爱。', '今天也要加油哦。',
    '祝你今天愉快。', '爱你么么哒。', '照顾好你的小情绪。', '世界很大，慢慢来。',
    '你值得更好的。', '不要难过。', '一切都会好起来的。', '记得想我哦。',
    '给你一个大大的拥抱。', '做一个善良的人。', '保持对生活的热爱。', '未来可期。',
    '你就是我的唯一。', '不要放弃梦想。', '努力成为更好的自己。', '你真的很特别。',
    '愿你一生平安。', '所有的好运都给你。', '你要幸福。', '爱你一万年。',
    '不离不弃。', '你就是我的小太阳。', '带给你温暖。', '一起加油。',
    '做一个温柔的人。', '愿你被世界温柔对待。', '好运连连。'
]

colors = [ 
    '#FFC0CB', '#ADD8E6', '#98FB98', '#FFFACD', '#FFB6C1', '#87CEEB',
    '#E0FFFF', '#FAFAD2', '#D8BFD8', '#E6E6FA', '#FFE4E1', '#F0FFF0'
]

all_popups = []
heart_n = 200 
scatter_n = 300 
delay = 0.01

def close_all(): 
    for popup in all_popups:
        popup.destroy()
    root.quit()

def create_popup(text, x, y, bg): 
    popup = tk.Toplevel(root)
    all_popups.append(popup)
    popup.overrideredirect(True)
    popup.attributes("-topmost", 1)
    popup.geometry(f"+{x}+{y}")
    popup.configure(bg=bg)
    label = tk.Label(popup, text=text, font=('Arial', 14), fg='black', bg=bg, padx=10, pady=5)
    label.pack()
    popup.bind('<space>', lambda e: close_all())
    popup.bind('<Escape>', lambda e: close_all())

def calculate_heart_coords(n, sw, sh): 
    coords = []
    scale_factor = min(sw, sh) / 35
    for i in range(n):
        t = (i / n) * 2 * math.pi
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        sx = int(sw / 2 + x * scale_factor)
        sy = int(sh / 2 - y * scale_factor)
        coords.append((sx, sy))
    return coords

def main(): 
    global root
    root = tk.Tk()
    root.withdraw()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    heart_coords = calculate_heart_coords(heart_n, sw, sh)
    for coord in heart_coords:
        text = random.choice(texts)
        bg = random.choice(colors)
        create_popup(text, coord[0], coord[1], bg)
        root.update()
        time.sleep(delay)
    for _ in range(scatter_n):
        rx = random.randint(0, sw - 150)
        ry = random.randint(0, sh - 40)
        text = random.choice(texts)
        bg = random.choice(colors)
        create_popup(text, rx, ry, bg)
        root.update()
    root.mainloop()

if __name__ == "__main__":
    main()
