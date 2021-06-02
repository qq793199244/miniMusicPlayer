import os
from pygame import mixer
from tkinter import filedialog, Tk, Listbox, END, ACTIVE, Button, messagebox


class MusicPlayer:
    # 导入
    def openfile(self):
        # 播放路径
        path = filedialog.askdirectory(initialdir="/", title="选择音乐文件夹")
        os.chdir(path)
        song = os.listdir()

        for s in song:
            try:
                if s.endswith(("mp3", "flac", "wav", "wma", "ape", "m4a")):
                    playlist.insert(END, s)
            except:
                messagebox.showinfo("提示", "文件格式不兼容，请重新选择文件夹。")

    # 播放
    def playsong(self):
        currentsong = playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        mixer.music.play()

    # 暂停
    def pausesong(self):
        mixer.music.pause()

    # 停止
    def stopsong(self):
        mixer.music.stop()

    # 继续
    def resumesong(self):
        mixer.music.unpause()


if __name__ == '__main__':
    # 为应用程序创建UI
    root = Tk()
    root.title('极简MusicPlayer')

    fc = MusicPlayer()

    # 播放列表。从系统中存储和显示歌曲列表。
    mixer.init()  # 检查系统中所有当前的歌曲
    playlist = Listbox(root, bg='white')
    playlist.grid(columnspan=10)

    Button(root, text='导入', command=fc.openfile).grid(row=1, column=0)
    Button(root, text='播放', command=fc.playsong).grid(row=1, column=1)
    Button(root, text='暂停', command=fc.pausesong).grid(row=1, column=2)
    Button(root, text='继续', command=fc.resumesong).grid(row=1, column=3)
    Button(root, text='停止', command=fc.stopsong).grid(row=1, column=4)

    root.mainloop()
