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
   
    def getConfig(self):
        return self.data.get("config", {})
   
    def saveConfig(self, config):
        self.data["config"] = config
        self.save()
   
    def save(self):
        with open(self.file_path, 'w',encoding='utf-8') as file:
            file.write('')
            json.dump(self.data, file)
  
    def get_shool_list(self):
        response = requests.get(urls.school_list_url, headers=headers.HEADERS_GET_SCHOOL)
        return response.json()
  
    def getMatchSchool(self, school_name,school_list):
        school_list = [school for school in school_list if school_name in school["name"]]
        if len(school_list) == 0:
            print(f"School {school_name} not found.")
            return None
        return school_list
   
    def selectSchool(self, school_list):
        print("Please select the school you want to join:")
        for i, school in enumerate(school_list):
            print(f"{i+1}. {school['name']}")
        n = input("Please enter the number of the school you want to join:")
        if(n.isdigit() and 1 <= int(n) <= len(school_list)):
            return school_list[int(n)-1]
        else:
            return None
 
    def getSID(self, school_name):
        print(f"Searching for schools with the name {school_name}...")
        school_list = requests.get(urls.school_list_url, headers=headers.HEADERS_GET_SCHOOL).json()
        matchSchoolList = []
        while not matchSchoolList:
            matchSchoolList = self.getMatchSchool(school_name, school_list)
        if len(school_list) > 1:
            selectedSchool = self.selectSchool(matchSchoolList)
        elif len(school_list) == 1:
            selectedSchool = school_list[0]
        else:
            print("No schools found.")
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