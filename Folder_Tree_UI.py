import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

def build_tree(root, indent=""):
    """建立只包含資料夾的樹狀結構字串"""
    tree_str = ""
    # 只取得目錄中的資料夾
    dirs = sorted([d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))])
    for index, item in enumerate(dirs):
        path = os.path.join(root, item)
        if index == len(dirs) - 1:
            tree_str += indent + "└── " + item + "\n"
            new_indent = indent + "    "
        else:
            tree_str += indent + "├── " + item + "\n"
            new_indent = indent + "│   "
        tree_str += build_tree(path, new_indent)
    return tree_str

def main():
    # 初始化 tkinter 並隱藏主視窗
    root = tk.Tk()
    root.withdraw()

    # 使用對話框選擇資料夾
    folder_path = filedialog.askdirectory(title="選擇資料夾")
    
    if folder_path:
        tree_structure = folder_path + "\n" + build_tree(folder_path)
        
        # 建立新的視窗顯示樹狀結構
        display_window = tk.Toplevel()
        display_window.title("資料夾樹狀結構")
        
        text_area = scrolledtext.ScrolledText(display_window, wrap=tk.WORD, width=80, height=30)
        text_area.insert(tk.INSERT, tree_structure)
        text_area.configure(state='disabled')  # 設定為唯讀
        text_area.pack(expand=True, fill='both')
        
        # 定義視窗關閉時的行為，按下叉叉後結束所有視窗及程式
        def on_close():
            display_window.destroy()
            root.destroy()
        
        display_window.protocol("WM_DELETE_WINDOW", on_close)
        display_window.mainloop()
    else:
        print("未選擇任何資料夾。")

if __name__ == '__main__':
    main()
