### 一个支持多线程暴力报名的命令行版PU口袋校园自动报名工具

### 本脚本已终止维护，使用pyside开发的UI界面版链接：https://github.com/fengnightstarts/pu_client

基于PU网页版模拟HTTP请求实现的PU

少量代码参考自：https://github.com/RedForestLonvor/PU-SignUpBot

基本上实现了自动报名、自行登录、列出所有可报名活动、根据学院过滤、报名的功能

本人第一次写脚本，有问题还请见谅,请各位积极反馈一下

release使用方式：双击直接运行

### 使用教程：

首次使用输入账号密码和学校

若匹配到多个学校请输入序号

配置是否自动登录，为true再次打开该程序会自动登录，否则会进入登陆选项界面，该界面可以修改用户和配置

modify user/config：修改用户信息和配置

用户信息会保存在程序目录下的 data.json 中，若出现问题可删除该文件

输入学院部分请输入你的学院全称或者子串。

例：学院全称为：“计算机科学与工程学院” 你可以输入全称或“计算机”，但是不要输入“计院/计算机学院”

“土木工程与建筑学院”可以输入“土木”、“土木工程”，但是不要输入“土建”

注意：除非你学院名称里有，否则不要输入标点符号或空格！

该部分也可以可以留空，请注意：本脚本使用改名称过滤活动，切记不要输错！

登陆失败一两次或卡在“尝试登录”较长时间为正常现象 尤其是用户刚抓取完活动列表之后就退出尝试重新登录时请耐心等待

登陆后会检测是否有已保存的活动列表，若存在会让你选择是否开始报名/抓取活动信息且不报名/删除列表，该列表会保存在target里

list all/filter/target 列出全部或过滤、加入报名名单的活动列表

首次list all或list target降自动抓取活动列表

注意，本脚本不会自动更新活动列表，若想重新抓取请使用flush命令。为保证你你会被服务器ban，请不要频繁刷新！

若list filter列表为空可能是由于没有你的学院能报名的活动，若你十分确认你学院有可报名的活动，请检查你的学院是否输入错误或者使用list all

注意：序号是你想报名的活动在上次list列表中的序号！请先list再添加活动！

使用 add 活动序号 添加活动至报名列表

输入 del 活动序号 从target列表中删除活动，但是fire过后即使删除了活动也不会停止报名，因此fire之前请使用list target检查活动是否有误

活动序号为你想报名的活动在上次list的活动名单中的序号，无需加括号

例如：你list filter之后，想报名该列表中的第一个活动，请输入add 1

随后你list all，你想报名all中的第3个活动，请输入
add 3

随后输入fire开始报名

也可以使用save命令将当前target列表保存到本地

保存的列表将在下次打开本脚本时自动读取

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
