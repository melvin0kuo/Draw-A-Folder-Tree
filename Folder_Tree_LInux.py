import os
import sys
import argparse

def print_tree(root, indent=""):
    """僅列出資料夾的樹狀結構"""
    # 過濾出目錄中僅含資料夾的項目，並排序以確保輸出順序一致
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

def main():
    parser = argparse.ArgumentParser(description="列出指定資料夾的樹狀結構（僅顯示資料夾）")
    parser.add_argument("folder_path", nargs="?", help="要列出樹狀結構的資料夾路徑")
    args = parser.parse_args()

    # 若命令列未提供路徑，則要求使用者輸入
    if args.folder_path:
        folder_path = args.folder_path
    else:
        folder_path = input("請輸入資料夾路徑: ").strip()
    
    if not folder_path or not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("輸入的路徑不存在或不是一個資料夾。")
        sys.exit(1)
    
    print(folder_path)
    print_tree(folder_path)

if __name__ == '__main__':
    main()
