import os

def print_tree(root, indent=""):
    """僅列出資料夾的樹狀結構"""
    # 過濾出僅包含資料夾的項目，並排序以確保輸出一致
    dirs = sorted([d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))])
    for index, item in enumerate(dirs):
        path = os.path.join(root, item)
        if index == len(dirs) - 1:
            print(indent + "└── " + item)
            new_indent = indent + "    "
        else:
            print(indent + "├── " + item)
            new_indent = indent + "│   "
        # 遞迴列出子資料夾
        print_tree(path, new_indent)

if __name__ == '__main__':
    folder_path = input("請輸入資料夾路徑: ").strip()
    if folder_path and os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(folder_path)
        print_tree(folder_path)
    else:
        print("輸入的路徑不存在或不是一個資料夾。")
