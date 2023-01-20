import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import *
import os,sys
import yaml
import io
from tkinter import messagebox
from tkinter import filedialog
import webbrowser

conf = f"{__file__}/data/config.yml"

def bug_report():
    ret = messagebox.askyesno('確認', 'ウェブブラウザでページを開きます。')
    if ret == True:
        webbrowser.open("https://github.com/sonyakun/AviUtl-App-Manager/issues")

def aviutl_install():
    print

def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    sv.set(iDirPath)
    if os.path.exists(f"{__file__}/data/") == True:
        with open(os.path.join(f"{__file__}/data/", "config.yml")) as f:
            data = yaml.safe_load(f)
            data["SETTING"]["PATH"]["AVIUTLPATH"] = iDirPath
    else:
        os.makedirs(f"{__file__}/data/")
        with open(os.path.join(f"{__file__}/data/", "config.yml")) as f:
            data = yaml.safe_load(f)
            data["SETTING"]["PATH"]["AVIUTLPATH"] = iDirPath


root = ThemedTk()
root.title("AviUtl-AppManager")

s = ttk.Style()
s.theme_use('black')

# Notebookウィジェットの作成
notebook = ttk.Notebook(root)

# タブの作成
aviutl = tk.Frame(notebook, bg='black')
plugins = tk.Frame(notebook, bg='black')
settings = tk.Frame(notebook, bg='black')

# notebookにタブを追加
notebook.add(aviutl, text="AviUtl")
notebook.add(plugins, text="プラグイン")
notebook.add(settings, text="設定", underline=0)

label = ttk.Label(aviutl, text="AviUtl", foreground="white")
label.pack()
label1 = ttk.Label(aviutl, text="AviUtlのファイルパス", foreground="white")
label1.pack()
sv = tk.StringVar()
entry1 = tk.Entry(aviutl, textvariable=sv)
entry1.pack()
IDirButton = ttk.Button(aviutl, text="参照", command=dirdialog_clicked)
IDirButton.pack()
Install_Avi_Button = ttk.Button(aviutl, text="インストール", command=aviutl_install)
Install_Avi_Button.pack()

bug_r = ttk.Label(settings, text="バグ報告", foreground="white")
bug_r.pack()
report_bug = ttk.Button(settings, text="Githubで報告", command=bug_report)
report_bug.pack()

notebook.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()