import threading
import datetime
import time
def single_acctivity(acts:list, Acc):
    threads = []
    for act in acts:
        Acc.flag[act.id] = False
        thread = threading.Thread(target=single, args=(act,Acc,acts))
        threads.append(thread)
        thread.start()
    # for thread in threads:
    #     thread.join()
        
def single(act,Acc,acts):
    threads = []
    nowTime = datetime.datetime.now()
    assert isinstance(nowTime, datetime.datetime), f"bot.single Error: nowTime不为datetime: {nowTime}, {type(nowTime)}"
    print(f"nowTime:{nowTime}")
    gap = act.joinStartTime - nowTime
    if gap.total_seconds() > 1.5:
        print(f"活动:{act.name}未开始报名,等待{gap.total_seconds()}秒")
        time.sleep(gap.total_seconds() - 1.5)
    for i in range(4):
        # time.sleep((act.joinStartTime - datetime.datetime.now()).total_seconds()*random.random(0.3,0.8))
        try:
            thread = threading.Thread(target=Acc.signup, args=(act,))
            thread.start()
            threads.append(thread)
        except Exception as e:
            print(f"活动:{act.name}线程启动异常, i={i}")
    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            print(f"活动:{act.name}某线程异常")
    if Acc.flag[act.id]:
        print(f"活动:{act.name}报名成功")
    else:
        print(f"活动:{act.name}报名失败")
    acts.remove(act)