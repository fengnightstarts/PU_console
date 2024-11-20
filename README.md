### 一个支持多线程暴力报名的命令行版PU

基于PU网页版模拟HTTP请求实现的PU

少量代码参考自：https://github.com/RedForestLonvor/PU-SignUpBot

基本上实现了自动报名、自行登录、列出所有可报名活动、根据学院过滤、报名的功能

由于本人实在不想写了功能可能没有完善

本人第一次写脚本，有问题还请见谅

尚未测试多线程爆破功能。。。

有问题还请各位积极反馈一下

release使用方式：双击直接运行

源码使用教程：

环境要求：Python 3.13+  requests库

3.13以下尚未测试

若未安装requests库，命令行执行：

'''
pip install requests
'''

双击app.py或进入脚本主目录执行：

'''
python app.py
'''

按照提示操作
注：autoLogin 为是否自动登录

登陆成功后会自动获取活动列表

获取成功后先list filter 随后可以add （序号）添加至报名列表

随后fire以开始报名
