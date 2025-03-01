# 資料夾樹狀結構工具

這個專案提供三種不同的工具來顯示資料夾的樹狀結構。所有工具都會僅顯示資料夾，不顯示檔案。

## 功能簡介

- 以樹狀結構呈現資料夾的階層關係
- 三種不同的操作方式：基本版、命令列參數版、圖形化介面版
- 僅顯示資料夾，不包含檔案
- 按照字母順序排序資料夾名稱

## 環境配置

### 基本需求

1. 安裝 Python 3.x：
   - Windows: 從 [Python 官網](https://www.python.org/downloads/) 下載並安裝
   - macOS: 使用 Homebrew 安裝 `brew install python`
   - Linux: 大多數發行版已預裝，或使用包管理器安裝 (例如 `sudo apt install python3`)

2. 確認 Tkinter 是否已安裝 (僅 Folder_Tree_UI.py 需要)：
   - 大多數 Python 安裝包已包含 Tkinter
   - 驗證方法：開啟 Python 命令列並輸入
     ```python
     import tkinter
     tkinter._test()
     ```
   - 如未安裝：
     - Windows/macOS: 重新安裝 Python 並選擇包含 Tkinter
     - Linux: `sudo apt-get install python3-tk` (Ubuntu/Debian)

### 虛擬環境 (選擇性)

建議使用虛擬環境以避免依賴衝突：

```bash
# 建立虛擬環境
python -m venv folder_tree_env

# 啟動虛擬環境
# Windows
folder_tree_env\Scripts\activate
# macOS/Linux
source folder_tree_env/bin/activate

# 退出虛擬環境
deactivate
```

## 檔案說明

### 1. Folder_Tree.py

基本版本，透過命令列輸入要查看的資料夾路徑。

```bash
python Folder_Tree.py
```

執行後會提示您輸入資料夾路徑，然後在命令列中顯示樹狀結構。

### 2. Folder_Tree_LInux.py

具備命令列參數功能的版本，可以直接指定路徑或稍後輸入。

```bash
# 直接指定路徑
python Folder_Tree_LInux.py /path/to/folder

# 或執行後輸入路徑
python Folder_Tree_LInux.py
```

### 3. Folder_Tree_UI.py

圖形化介面版本，使用 Tkinter 提供資料夾選擇對話框和結果顯示視窗。

```bash
python Folder_Tree_UI.py
```

執行後會彈出資料夾選擇對話框，選擇後會在新視窗中顯示樹狀結構結果。

## 使用範例

基本版輸出範例：

```
D:\Projects
├── WebDev
│   ├── React
│   └── Vue
└── Python
    ├── DataScience
    └── WebScraping
```

## 系統需求

- Python 3.x
- Tkinter (圖形化介面版本需要，通常已包含在 Python 標準庫中)

## 安裝方式

1. 確保已安裝 Python 3.x
2. 下載專案中的三個 Python 檔案
3. 無需額外安裝套件

## 故障排除

- **Error: ModuleNotFoundError: No module named 'tkinter'**
  - 解決方法：按照上方環境配置安裝 Tkinter

- **Error: Permission denied**
  - 解決方法：確保您有足夠權限訪問指定的資料夾

- **顯示亂碼**
  - 解決方法：確認終端機使用 UTF-8 編碼

## 使用建議

- 對於簡單的目錄結構查看，使用 `Folder_Tree.py`
- 需要命令列整合時，使用 `Folder_Tree_LInux.py`
- 需要圖形化介面時，使用 `Folder_Tree_UI.py`

## 授權條款

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
