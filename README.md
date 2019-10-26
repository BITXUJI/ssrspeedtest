# ssrspeedtest
ssr测速，支持ssr：//的txt文件输入和gui-config.json输入，返回可用的相应文件，并给节点标注带宽信息。
生成文件在temp子文件夹中
### 目前仅针对Windows 用户
```
pip install PySocks prettytable requests 
# 把master分支打包下载并进入程序目录  (cd C:\Users\Dell\Downloads\ssrspeedtest-master)
# 使用.json配置文件测速
python ssr_speed_win.py gui-config.json(加上配置文件后不用输入订阅链接)
#使用包含ssr://的.txt文件测速
python ssr_speed_win.py ssr.txt
# 使用SSR订阅链接测速
python ssr-speed_win.py
url: //输入入SSR订阅链接
```
