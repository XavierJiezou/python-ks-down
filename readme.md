# Introduction
A small program for downloading [kuaishou](https://www.kuaishou.com/) short videos (without watermark) , which is made with Python.
# Demo
![demo.gif](demo.gif)
# Install
```bash
pip install requests tqdm
```
# Usage
```bash
git clone https://github.com/XavierJiezou/python-ks-down.git
cd python-ksdown
python down.py
```
Input a video url from [kuaishou](https://www.kuaishou.com/), like: [https://v.kuaishou.com/5i7XWC](https://v.kuaishou.com/5i7XWC).
```bash
请输入复制的快手分享链接：https://v.kuaishou.com/5i7XWC
正在请求，预计需要3秒：
100%|█████████████| 6/6 [00:00<00:00, 1983.12KB/s]
下载完成，总计用时3秒。
```
# Unpack
```bash
git clone https://github.com/XavierJiezou/python-ks-down.git
cd python-ksdown
pipenv install
pipenv shell
pip install requests tqdm
pip install pyinstaller
pyinstaller -F -i favicon.ico down.py
```
Building EXE is placed in the `dist` folder.
# Download

