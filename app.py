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
        acc.login(user)
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
    list_type = "all"
    all_list = acc.get_activity_list()
    all_list.sort(key=lambda act: act.joinStartTime)
    filter_list = acc.get_filter_list(all_list)
    target_list = []
    while True:
        print("指令列表")
        print("list all 列出所有未开始报名或已开始报名但未满员的活动")
        print("list filter 列出所自己学院可以报名的活动")
        print("list target 列出已选择的活动")
        print("info")
        print("back")
        print("fire 开始报名")
        print("add [act index] 添加活动到target")
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
            value = input("is autoLogin? True/False")
            config["autoLogin"] = bool(value)
            value = input("myCollege")
            config["myCollege"] = value
            value = input("credit")
            config["credit"] = int(value)
            manager.saveConfig(config)
        elif choice_split[0] == "back":
            return
        
def add_act(all_list, filter_list, list_type, target_list, index):
    i = int(index)
    if list_type == "all":
        if i > len(all_list):
            print("invalid input")
            return
        target_list.append(all_list[index - 1])
    elif list_type == "filter":
        if i > len(filter_list):
            print("invalid input")
            return
        target_list.append(filter_list[index - 1])
        
def list(split_choice, all_list, filter_list, target_list):
    if len(split_choice) == 0:
        print("invalid input")
        return
    if split_choice[0] == "all":
        acts = all_list
    elif split_choice[0] == "filter":
        acts = filter_list
    elif split_choice[0] == "target":
        acts = target_list
    for i,act in enumerate(acts, start = 1):
        print(i,": ",act.name," credit:",act.credit," 是否已报名:",act.hasJoin)
        print("    joinStartTime:",act.joinStartTime)
        print("    startTime:",act.startTime)
        print("    endTime:",act.endTime)
        print("    category: ",act.categoryName, " address:",act.address)
        print("    allowUserCount:",act.allowUserCount)
        print("    joinUserCount:",act.joinUserCount)
        if act.allowCollege == []:
            print("    allowCollege: all")
        else:
            print("    allowCollege:",act.allowCollege)

if __name__ == "__main__":
    main()