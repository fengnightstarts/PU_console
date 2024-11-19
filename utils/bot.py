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
    if gap.total_seconds() > 5:
        time.sleep(gap.total_seconds() - 5)
    for i in range(5):
        thread = threading.Thread(target=Acc.signup, args=(act,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    if Acc.flag.get(act.id) == True:
        print(f"报名成功,活动:{act.name}")