from utils import user_data_manager
from utils import account
from utils import bot
from utils import activity
config = {}
user = {}
# config = {}
acc = None
manager = None
def main():
    print("欢迎使用PU_console")
    print("项目地址：https://github.com/fengnightstarts/PU_console")
    print("作者：fengnightstarts")
    print("有问题请到项目地址提")
    global user
    global config
    global acc
    global manager
    flag = True
    manager = user_data_manager.UserDataManager(file_path="data.json")
    user = manager.getUserData()
    config = manager.getConfig()
    acc = account.Account()
    while True:
        if config == {}:
            config = {
                "autoLogin":False,
                "myCollege":"",
                "credit":0,
                "categoreis":[],
            }
        manager.saveConfig(config)
        activity.rules["college"] = config["myCollege"]
        if user == {}:
            print("请创建用户")
            user = manager.createUser()
            print("please create config")
            modify_config(config)
        if config["autoLogin"] and flag:
            flag = False
            if acc.login(user):
                main_menu(acc, user, config)
        else:
            login_menu(user, manager, acc, config)
        
def modify_config(config):
    value = input("是否自动登录？ True/False")
    config["autoLogin"] = bool(value)
    value = input("请输入学院名称\n 正确示例:计算机科学与工程学院/计算机\n错误输入:计算机学院\n")
    config["myCollege"] = str(value)
    manager.saveConfig(config)
    activity.rules["college"] = config["myCollege"]
    
def login_menu(user, manager, acc, config):
    while True:
        print("info")
        print("modify user")
        print("modify config")
        print("login")
        choice = input("请输入你的选择：")
        if choice == "info":
            print(user)
            print(config)
        elif choice == "modify user":
            manager.createUser()
        elif choice == "login":
            if acc.login(user):
                main_menu(acc, user, config)
            else:
                print("登录失败")
        elif choice == "modify config":
            print(config)
            modify_config(config)
        else:
            print("错误选项")
            
def main_menu(acc, user, config):
    list_type = "filter"
    all_list = acc.get_activity_list()
    all_list.sort(key=lambda act: act.joinStartTime)
    filter_list = acc.get_filter_list(all_list)
    target_list = []
    list(["filter"], all_list, filter_list,target_list)
    
    while True:
        print("指令列表")
        print("list all 列出所有未开始报名或已开始报名但未满员的活动")
        print("list filter 列出所自己学院可以报名的活动")
        print("list target 列出已选择的活动")
        print("info 查看用户信息")
        print("back 返回上一级")
        print("fire 开始报名")
        print("add index 添加活动到target")
        print("del index 删除target中的活动(不支持删除已经fire的活动)")
        
        choice = input("请输入你的选择：")
        choice_split = choice.split()
        
        if choice_split[0] == "list":
            list(choice_split[1:], all_list, filter_list, target_list)
            if choice_split[1] == "all":
                list_type = "all"
            elif choice_split[1] == "filter":
                list_type = "filter"
                
        elif choice_split[0] == "info":
            print(user)
            print(acc.token)
            print(config)
            
        elif choice_split[0] == "add":
            add_act(all_list, filter_list, list_type, target_list, int(choice_split[1]))
            
        elif choice_split[0] == "fire":
            bot.single_acctivity(target_list,acc)
            
        elif choice_split[0] == "modify":
            value = input("是否自动登录 True/False")
            config["autoLogin"] = bool(value)
            value = input("请输入学院名称")
            config["myCollege"] = value
            manager.saveConfig(config)
            
        elif choice_split[0] == "del":
            del_act(target_list, choice_split[1])
            
        elif choice_split[0] == "back":
            return
        else:
            print("输入错误")

def del_act(target_list, index):
    i = int(index)
    if i > len(target_list) or i < 1:
        print("序号超限")
    else:
        target_list.pop(i - 1)
        
def add_act(all_list, filter_list, list_type, target_list, index):
    
    i = int(index)
    
    if list_type == "all":
        if i > len(all_list):
            print("输入错误")
            return
        target_list.append(all_list[index - 1])
        
    elif list_type == "filter":
        if i > len(filter_list):
            print("输入错误")
            return
        target_list.append(filter_list[index - 1])
        
def list(split_choice, all_list, filter_list, target_list):
    if len(split_choice) == 0:
        print("错误输入")
        return
    if split_choice[0] == "all":
        acts = all_list
    elif split_choice[0] == "filter":
        acts = filter_list
    elif split_choice[0] == "target":
        acts = target_list
    for i,act in enumerate(acts, start = 1):
        
        print(i,": ",act.name," PU分值:",act.credit," 是否已报名:",act.hasJoin)
        print("    报名开始时间:",act.joinStartTime)
        print("    活动开始时间:",act.startTime)
        print("    活动结束时间:",act.endTime)
        print("    活动类别: ",act.categoryName, " 活动地点:",act.address)
        print("    活动人数:",act.allowUserCount)
        print("    已报名人数:",act.joinUserCount)
        
        if act.allowCollege == []:
            print("    活动学院: 全部")
        else:
            print("    活动学院:",act.allowCollege)

if __name__ == "__main__":
    main()