# 软件下载
> win64：[https://ghgxj.lanzous.com/iABghjltmpg](https://ghgxj.lanzous.com/iABghjltmpg)

`win32`、`mac`和`linux`用户请自行通过源码打包。
# 使用教程
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201222175941134.gif#pic_center)
# 完整代码
```python
import re
import requests
from tqdm import tqdm
inp = input('请输入复制的快手分享链接：')  # https://v.kuaishou.com/5i7XWC
url = re.findall('https://v.kuaishou.com/\w{6}', inp)[0]
headers = {
    'User-Agent': 'Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
}
res = requests.get(url, headers=headers)
url = re.findall('src="(.*?)"', res.text)[0]
res = requests.get(url)
total_size = round(int(res.headers["Content-Length"])/1024/1024)
with open('vid.mp4', 'wb') as f:
    for chunk in tqdm(iterable=res.iter_content(1024*1024), total=total_size, unit='KB'):
        f.write(chunk)
```
# 样例输入
> 快手短视频分享链接：[https://v.kuaishou.com/5i7XWC](https://v.kuaishou.com/5i7XWC)

1、点击**分享**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201222180259697.png?x-oss-process=image,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyOTUxNTYw,size_16,color_FFFFFF,t_70)

2、点击**复制链接**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201222180358425.png?x-oss-process=image,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyOTUxNTYw,size_16,color_FFFFFF,t_70)

3、将复制的文本作为程序的**输入**
```bash
#动漫 #别限流 #漫剪番名:《人马少女的烦恼》BGM:你是对的人 为什么有人就是不愿意看这里呀 https://v.kuaishou.com/8WFShS 复制此消息，打开【快手】直接观看！
```
----
**注意**：你可以将复制的链接作为程序的输入，也可以将整个文本作为程序的输入，因为第**5**行代码会对输入进行解析：
```python
url = re.findall('https://v.kuaishou.com/\w{6}', inp)[0]
```
# 样例输出
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201222181306794.gif#pic_center)

# 打包教程
> 【python】将代码打包为软件：[https://blog.csdn.net/qq_42951560/article/details/111086049](https://blog.csdn.net/qq_42951560/article/details/111086049)
# 温馨提示
水印本质上是对版权的一种保护，本文提供的方法仅供学习交流，请勿非法商用，如果你想转载抖音视频，请征求原作者的同意，并注明出处，拒绝营销。
# 相关推荐
> 【python】15行代码下载抖音无水印短视频：[https://blog.csdn.net/qq_42951560/article/details/111085969](https://blog.csdn.net/qq_42951560/article/details/111085969)
