import json
from utils import urls
import requests
from utils import headers
class UserDataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with open(file_path, 'r',encoding='utf-8') as file:
                self.data = json.load(file)
        except json.JSONDecodeError:
            print(f"The file {file_path} does not contain valid JSON or is empty.")
            self.data = {}
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
            self.data = {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.data = {}
 
    def getUserData(self):
        return self.data.get("user", {})
    def saveTargetList(self, target_list):
        self.data["target_list"] = [act.id for act in target_list]
        self.save()
    def get_target_list(self):
        return self.data.get("target_list", [])
    
    def getConfig(self):
        return self.data.get("config", {})
   
    def saveConfig(self, config):
        self.data["config"] = config
        self.save()
   
    def save(self):
        try:
            with open(self.file_path, 'w',encoding='utf-8') as file:
                file.write('')
                json.dump(self.data, file)
        except Exception as e:
            print("配置保存失败, 请检查程序是否有权限写入文件.若文件存在请删除该文件")
    # def get_shool_list(self):
    #     response = requests.get(urls.school_list_url, headers=headers.HEADERS_GET_SCHOOL)
    #     return response.json()
  
    def getMatchSchool(self, school_name,school_list):
        school_list = [school for school in school_list if school_name in school["name"]]
        if len(school_list) == 0:
            print(f"School {school_name} not found.")
            return None
        return school_list
   
    def selectSchool(self, school_list):
        print("以下是匹配到的学校列表:")
        for i, school in enumerate(school_list):
            print(f"{i+1}. {school['name']}")
        n = input("请输入学校序号, 序号从1开始: ")
        if(n.isdigit() and 1 <= int(n) <= len(school_list)):
            return school_list[int(n)-1]
        else:
            print("序号输入错误")
            return None
 
    def getSID(self, school_name):
        print(f"正在获取学校列表")
        school_list = requests.get(urls.school_list_url, headers=headers.HEADERS_GET_SCHOOL).json()
        if not school_list:
            print("获取学校列表失败, 请稍后再试")
            return None
        matchSchoolList = []
        matchSchoolList = self.getMatchSchool(school_name, school_list)
        if not matchSchoolList:
            return None
        if len(school_list) > 1:
            selectedSchool = self.selectSchool(matchSchoolList)
        elif len(school_list) == 1:
            selectedSchool = school_list[0]
        else:
            print("No schools found.")
            return None
        if not selectedSchool:
            return None
        return selectedSchool["go_id"]
  
    def createUser(self):
        user_name = input("请输入userName: ")
        password = input("请输入password: ")
        sid = None
        while not sid:
            school_name = input("请输入学校名称: ")
            sid = int(self.getSID(school_name))
        new_user = {
            'userName': user_name,
            'password': password,
            'sid': sid,
            'device': 'pc'
        }
        self.data["user"] = new_user
        self.save()
        return new_user