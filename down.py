import re
import os
import time
import requests
from tqdm import tqdm


def down():
    inp = input('请输入复制的快手分享链接：')  # https://v.kuaishou.com/5i7XWC
    t1 = time.time()
    url = re.findall('https://v.kuaishou.com/\w{6}', inp)[0]
    headers = {
        'User-Agent': 'Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }
    res = requests.get(url, headers=headers)
    url = re.findall('src="(.*?)"', res.text)[0]
    vid = re.findall('clientCacheKey=(.*?)&', url)[0]
    print(f'正在请求，预计需要3秒：')
    res = requests.get(url)
    total_size = round(int(res.headers["Content-Length"])/1024/1024)
    with open(vid, 'wb') as f:
        for chunk in tqdm(iterable=res.iter_content(1024*1024), total=total_size, unit='KB', ncols=50):
            f.write(chunk)
    t2 = time.time()
    print(f'下载完成，总计用时{t2-t1:.0f}秒。')
    os.system('pause')


if __name__ == '__main__':
    down()
