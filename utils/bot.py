from utils import account
from utils import activity
import threading
import datetime
import time
def single_account(acts, Acc):
    threads = []
    for act in acts:
        Acc.flag[act.id] = False
        for i in range(5):
            thread = threading.Thread(target=single, args=(act,Acc))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
        
def single(act,Acc):
    threads = []
    gap = act.joinStartTime - datetime.datetime.now()
    print(f"活动:{act.name}未开始报名,等待{gap.total_seconds()}秒")
    if  gap.total_seconds() > 90:
        print("等待时间过长, 为保证token有效, 将提前90sec重新尝试登陆")
        time.sleep(gap.total_seconds() - 90)
        if not Acc.login():
            print("登陆失败")
            return
    if gap.total_seconds() > 2:
        time.sleep(gap.total_seconds() - 2)
    for i in range(4):
        thread = threading.Thread(target=Acc.signup, args=(act,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    if Acc.flag.get(act.id) == True:
        print(f"报名成功,活动:{act.name}")