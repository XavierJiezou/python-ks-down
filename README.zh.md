简体中文 | [English](README.md)
# 简介
用Python制作的，一个下载[快手](https://www.kuaishou.com/)无水印短视频的小程序。
# 演示
![demo.gif](demo.gif)
# 安装
```bash
pip install requests tqdm
```
# 用法
1. 克隆仓库后运行`down.py`。
```bash
git clone https://github.com/XavierJiezou/python-ks-down.git
cd python-ks-down
python down.py
```
1. 输入[快手](https://www.kuaishou.com/)短视频的分享链接, 例如: [https://v.kuaishou.com/5i7XWC](https://v.kuaishou.com/5i7XWC)。
```bash
请输入复制的快手分享链接：https://v.kuaishou.com/5i7XWC
正在请求，预计需要3秒：
100%|█████████████| 6/6 [00:00<00:00, 1983.12KB/s]
下载完成，总计用时3秒。
```
3. [3xyaezs2t5k3srs_b.mp4](3xyaezs2t5k3srs_b.mp4)就是刚才那个测试链接下载的视频。
# 打包
```bash
git clone https://github.com/XavierJiezou/python-ks-down.git
cd python-ks-down
pipenv install
pipenv shell
pip install requests tqdm
pip install pyinstaller
pyinstaller -F -i favicon.ico down.py
```
---
注意：构建后的EXE文件放在`dist`文件夹中。
# 下载
> [ksdown-1.0.0-win64.exe](https://github.com/XavierJiezou/python-ks-down/releases/download/1.0.0/ksdown-1.0.0-win64.exe)
