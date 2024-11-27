import datetime
import time
import requests
from utils import headers, urls, activity
import threading
import random

class Account:
    def __init__(self):
        self.token = ""
        self.user_data = {}
        self.flag:dict = {"111":False}
        self.lock = threading.Lock()
        # self.loginTime = None
    def login(self, user_data_input):
        if user_data_input != None:
            self.user_data = user_data_input
        for i in range(5):
            print("尝试登陆")
            response = requests.post(urls.login_url, headers=headers.HEADERS_LOGIN, json=self.user_data)
            response.raise_for_status()
            # print(response.json())
            curToken = response.json().get("data", {}).get("token")
            print("登录尝试次数:", i+1)
            if curToken:
                self.token = curToken
                print("token = ", self.token)
                # self.loginTime = datetime.datetime.now()
                return curToken
            else:
                print("登录失败,返回信息：")
                print(response.text)
        print("登录失败,获取token失败")
        return None

    def signup(self, act, token=None):
        if not token:
            token = self.token
        data = {"activityId": act.id}
        header = headers.HEADERS_ACTIVITY.copy()
        header["Authorization"] = f"Bearer {self.token}" + ":" + str(self.user_data.get("sid"))
        gap = act.joinStartTime - datetime.datetime.now()
        if gap.total_seconds() > 1:
            time.sleep(gap.total_seconds()-1)
        if gap.total_seconds() > 0:
            time.sleep((act.joinStartTime - datetime.datetime.now).total_seconds()*random.random(1,1.5))
        i = 0
        while True:
            if self.flag[act.id]:
                break
            i+=1
            response = requests.post(url=urls.activity_url, headers=header, json=data)
            response.raise_for_status()
            if response.status_code == 200:
                print("请求成功,活动:",act.name , response.text, "请求时间:" ,datetime.datetime.now())
                if(response.text == '{"code":0,"message":"成功","data":{"msg":"PU君提示：报名成功，请留意活动签到时间哦~"}}'):
                    self.lock.acquire()
                    try:
                        self.flag[act.id] = True
                    finally:
                        self.lock.release()
                    break
                if(response.text == '{"code":9405,"message":"您已报名，请勿重复操作","data":{}}'):
                    self.lock.acquire()
                    try:
                        self.flag[act.id] = True
                    finally:
                        self.lock.release()
                    break
            if i < 5:
                time.sleep(0.1)
            elif i < 10:
                time.sleep(0.5 * random.uniform(0.8, 1.5))
            elif i < 15:
                time.sleep(2 * random.uniform(0.8, 1.5))
            elif i == 20:
                print("报名失败")
                break

    def get_activity_info(self, id):
        info_header = headers.HEADERS_ACTIVITY_INFO.copy()
        info_header["Authorization"] = f"Bearer {self.token}" + ":" + str(self.user_data.get("sid"))
        info_json = {"id": id}
        info_response = requests.post(url=urls.info_url, headers=info_header, json=info_json)
        info_response.raise_for_status()
        info_data = info_response.json().get("data", {}).get("baseInfo", {})
        act = activity.Activity(info_data,id,info_response.json().get("data", {}).get("userStatus").get("hasJoin"))
        return act

    def get_activity_list(self):
        list_header = headers.HEADERS_ALL_ACTIVITY.copy()
        list_header["Authorization"] = f"Bearer {self.token}" + ":" + str(self.user_data.get("sid"))
        list_json = {"sort": 1, "page": 1, "limit": 20}
        all_activity_data = []
        flag = False
        for i in range(1,12):
            list_json["page"] = i
            list_response = requests.post(url=urls.list_url, headers=list_header, json=list_json)
            list_response.raise_for_status()
            list_data = list_response.json().get("data", {}).get("list", [])
            flag = True
            if not list_data:
                print("没有活动了")
                break
            for act in list_data:
                if "报名未开始" in act["startTimeValue"] or ("报名进行中" in act["startTimeValue"] and act["joinUserCount"] < act["allowUserCount"]):
                    flag = False
                    time.sleep(0.1)
                    print(f"活动:{act['name']}报名未开始或报名人数未满，正在获取详细信息")
                    all_activity_data.append(self.get_activity_info(act["id"]))
            if flag:
                break
        return all_activity_data

    def get_filter_list(self, all_act_list):
        filter_list = []
        for act in all_act_list:
            if act.filter():
                filter_list.append(act)
        return filter_list