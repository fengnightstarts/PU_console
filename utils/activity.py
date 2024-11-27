import datetime
#"userStatus":{"hasJoin":1,"hasSignIn":0,"hasSignOut":0,"hasFinish":0,"hasXinde":0},
class Activity:
    def __init__(self, info_data,id,hasJoin):
        self.id = id
        self.name = info_data.get("name")
        self.credit = info_data.get("credit")
        self.joinStartTime = self.parse_datetime(info_data.get("joinStartTime"))
        self.joinEndTime = self.parse_datetime(info_data.get("joinEndTime"))
        self.startTime = self.parse_datetime(info_data.get("startTime"))
        self.endTime = self.parse_datetime(info_data.get("endTime"))
        self.address = info_data.get("address")
        self.categoryName = info_data.get("categoryName")
        self.allowCollege = [college["name"] for college in info_data.get("allowCollege")]
        self.allowYear = [year["name"] for year in info_data.get("allowYear")]
        self.allowUserType = info_data["allowUserType"]
        self.joinType = info_data["joinType"]
        self.allowUserCount = info_data["allowUserCount"]
        self.joinUserCount = info_data["joinUserCount"]
        self.hasJoin = hasJoin
    def parse_datetime(self, date_str):
        if date_str:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return None

    def is_allow(self):
        # and act["allowUserType"] == 1 and act["joinType"] == 1
        if self.allowUserType != 1 or self.joinType != 1:
            return False
        if self.allowCollege == []:
            return True
        for item in self.allowCollege:
            if rules.get("college", "") in item:
                return True
        return False
  
    def filter(self):
        return self.is_allow() and rules.get("categoryName", "") in self.categoryName and self.hasJoin == 0
   
    def __str__(self):
        return (f"name={self.name}, credit={self.credit}, "
                f"joinStartTime={self.joinStartTime}, startTime={self.startTime}, "
                f"endTime={self.endTime}, address={self.address}, categoryName={self.categoryName})")

rules = {}