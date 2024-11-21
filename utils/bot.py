import threading
import datetime
import time
def single_acctivity(acts, Acc):
    threads = []
    for act in acts:
        Acc.flag[act.id] = False
        thread = threading.Thread(target=single, args=(act,Acc))
        threads.append(thread)
        thread.start()
    # for thread in threads:
    #     thread.join()
        
def single(act,Acc):
    threads = []
    gap = act.joinStartTime - datetime.datetime.now()
    print(f"活动:{act.name}未开始报名,等待{gap.total_seconds()}秒")
    if gap.total_seconds() > 1.5:
        time.sleep(gap.total_seconds() - 1.5)
    for i in range(4):
        # time.sleep((act.joinStartTime - datetime.datetime.now()).total_seconds()*random.random(0.3,0.8))
        thread = threading.Thread(target=Acc.signup, args=(act,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()