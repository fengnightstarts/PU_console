HEADERS_ACTIVITY_INFO = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Authorization": "",
    "Origin": "https://class.pocketuni.net",
    "Connection": "keep-alive",
    "Referer": "https://class.pocketuni.net/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

HEADERS_ACTIVITY = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Authorization": "",
        "Origin": "https://class.pocketuni.net",
        "Connection": "keep-alive",
        "Referer": "https://class.pocketuni.net/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
}
HEADERS_ALL_ACTIVITY = {
    "Connection": "keep-alive",
    "Content-Length": "30",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://class.pocketuni.net",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://class.pocketuni.net/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
# POST /apis/activity/list HTTP/1.1
# Host: apis.pocketuni.net
# Connection: keep-alive
# Content-Length: 30
# Authorization: Bearer 989f8926a4e311ef8ffb00163e010410:208754666766336
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
# Accept: application/json, text/plain, */*
# DNT: 1
# Content-Type: application/json
# Origin: https://class.pocketuni.net
# Sec-Fetch-Site: same-site
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://class.pocketuni.net/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6

# {"sort":0,"page":1,"limit":10}
HEADERS_LOGIN = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://class.pocketuni.net",
        "Connection": "keep-alive",
        "Referer": "https://class.pocketuni.net/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
}

HEADERS_GET_SCHOOL = {
        'sec-ch-ua':'"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-User':'?1',
        'Sec-Fetch-Dest':'document',
        'Referer':'https://pocketuni.net/',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}




# HTTP/1.1 200 OK
# Date: Sun, 17 Nov 2024 13:15:04 GMT
# Content-Type: application/json; charset=utf-8
# Connection: keep-alive
# Access-Control-Allow-Headers: Content-Type, Origin, X-CSRF-Token, Authorization, AccessToken, Token, Range
# Access-Control-Allow-Methods: GET, HEAD, POST, PATCH, PUT, DELETE
# Access-Control-Allow-Origin: https://class.pocketuni.net
# Access-Control-Expose-Headers: Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers
# Access-Control-Max-Age: 86400
# Traceparent: 00-184b47349e10c2e49541f4596cc29ab8-643a6ec304ab1694-00
# Vary: Origin
# Kong-Trace-ID: 37596290-73f5-4304-b157-1bebcc76e7ad
# vary: Origin
# Access-Control-Allow-Credentials: true
# X-Kong-Upstream-Latency: 16
# X-Kong-Proxy-Latency: 4
# Via: kong/3.2.2.5-enterprise-edition
# Content-Length: 4918

# {"code":0,"message":"成功","data":{"pageInfo":{"count":688,"total":69,"page":1,"limit":10},"list":[{"id":256632852774912,"name":"【校团委第二课堂】“六级模拟考，挑战英语高峰”活动","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_wtys.png","credit":2,"puAmount":0,"allowUserCount":200,"startTime":"2024-11-23 14:30:00","startTimeValue":"报名未开始","endTime":"2024-11-23 17:30:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 08:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":1},{"id":256631827267584,"name":"【校团委第二课堂】“四级模拟考，助力英语提升”活动","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_wtys.png","credit":2,"puAmount":0,"allowUserCount":200,"startTime":"2024-11-23 08:30:00","startTimeValue":"报名未开始","endTime":"2024-11-23 11:30:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 08:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":0},{"id":256416172933121,"name":"【经管学院】VIKpro\u0026山科小红书挑战赛","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_xscx.png","credit":1,"puAmount":0,"allowUserCount":600,"startTime":"2024-11-21 14:00:00","startTimeValue":"报名进行中","endTime":"2024-11-21 17:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-17 16:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":351},{"id":256414660624385,"name":"【校心健联】“心理成长计划系列活动”自我探索:MBTI工作坊","logo":"https://img.pocketuni.net/data/uploads/2024/1116/11/96016636-0ba8-4432-9592-c0ce4ab2dfd0.jpg","credit":2,"puAmount":0,"allowUserCount":30,"startTime":"2024-11-19 16:00:00","startTimeValue":"报名进行中","endTime":"2024-11-19 17:30:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-17 08:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":30},{"id":256407620812800,"name":"【能源学院】“墨色乌金”智汇科创科普活动","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_xscx.png","credit":1,"puAmount":0,"allowUserCount":100,"startTime":"2024-11-19 16:00:00","startTimeValue":"报名未开始","endTime":"2024-11-19 17:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 10:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":0},{"id":256333211762688,"name":"【安全学院安全24-1】“创出未来，闯出精彩”主题团课","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_ddxy.png","credit":1,"puAmount":0,"allowUserCount":35,"startTime":"2024-11-19 19:00:00","startTimeValue":"报名未开始","endTime":"2024-11-19 20:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 08:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":1},{"id":256266402856960,"name":"【校学生会权益部】校园食堂优秀服务档口评选","logo":"https://img.pocketuni.net/data/uploads/2024/1115/15/9ef7116e-c765-45db-a59b-09c444fb6e31.jpg","credit":2,"puAmount":0,"allowUserCount":2000,"startTime":"2024-11-19 12:00:00","startTimeValue":"报名进行中","endTime":"2024-11-20 19:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-17 13:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":2000},{"id":256265351725056,"name":"【安全学院环境24-3】“创出精彩，闯出未来”主题团课","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_ddxy.png","credit":1,"puAmount":0,"allowUserCount":30,"startTime":"2024-11-22 14:30:00","startTimeValue":"报名进行中","endTime":"2024-11-22 16:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-17 00:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":21},{"id":256248102649859,"name":"【经管学院】“科创逐梦，智启新程”科创经验分享讲座","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_xscx.png","credit":1,"puAmount":0,"allowUserCount":120,"startTime":"2024-11-23 16:00:00","startTimeValue":"报名未开始","endTime":"2024-11-23 17:30:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-22 10:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":1},{"id":256140481003521,"name":"【安全学院】“七五华诞逢盛世，竞赛之笔绘新篇” 慧智培训会","logo":"https://img.pocketuni.net/data/uploads/2024/1114/22/77d08ec6-6dc7-4fec-b371-8ffe8cd16ae5.jpg","credit":1,"puAmount":0,"allowUserCount":200,"startTime":"2024-11-19 16:00:00","startTimeValue":"报名进行中","endTime":"2024-11-19 18:00:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-15 22:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":200}]}}
# {"id":256631827267584,"name":"【校团委第二课堂】“四级模拟考，助力英语提升”活动","logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_wtys.png","credit":2,"puAmount":0,"allowUserCount":200,"startTime":"2024-11-23 08:30:00","startTimeValue":"报名未开始","endTime":"2024-11-23 11:30:00","statusName":"未开始","allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 08:00:00","work_upload":0,"signType":1,"puType":0,"joinUserCount":0},
# {"id":256631827267584,
#  "name":"【校团委第二课堂】“四级模拟考，助力英语提升”活动",
#  "logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_wtys.png",
#  "credit":2,
#  "puAmount":0,
#  "allowUserCount":200,
#  "startTime":"2024-11-23 08:30:00",
#  "startTimeValue":"报名未开始",
#  "endTime":"2024-11-23 11:30:00",
#  "statusName":"未开始",
#  "allowJoinCount":0,
#  "joinType":1,
#  "joinStartTime":"2024-11-18 08:00:00",
#  "work_upload":0,
#  "signType":1,
#  "puType":0,
#  "joinUserCount":0
#  }
# {"id":256407620812800,"name":"【能源学院】“墨色乌金”智汇科创科普活动",
#  "logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_xscx.png",
#  "credit":1,"puAmount":0,"allowUserCount":100,
#  "startTime":"2024-11-19 16:00:00","startTimeValue":"报名未开始",
#  "endTime":"2024-11-19 17:00:00","statusName":"未开始",
#  "allowJoinCount":0,"joinType":1,"joinStartTime":"2024-11-18 10:00:00",
#  "work_upload":0,"signType":1,"puType":0,"joinUserCount":0},

# {"code":0,"message":"成功","data":
#         {"baseInfo":
#                 {"name":"【校团委第二课堂】“六级模拟考，挑战英语高峰”活动",
#                  "logo":"https://img.pocketuni.net//lzlg/sys_pic/activity_wtys.png",
#                  "creatorName":"sdust超管","creatorUID":2092123,"statusName":"未开始",
#                  "categoryId":208776145732452,"categoryName":"文化艺术与身心发展",
#                  "subCategoryId":0,"levelId":0,"levelName":"","credit":2,"puAmount":0,
#                  "joinStartTime":"2024-11-18 08:00:00","joinEndTime":"2024-11-23 08:00:00",
#                  "startTime":"2024-11-23 14:30:00","endTime":"2024-11-23 17:30:00",
#                  "address":"J5-302","allowUserCount":200,"joinUserCount":1,
#                  "signInUserCount":1,"signOutUserCount":1,
#                  "description":"为我校学生提供一次接近真实六级考试环境的模拟测试，帮助学生熟悉考试流程、题型和时间安排，发现自身英语学习的不足，为正式六级考试做好充分准备。山东科技大学校团委第二课堂特举办山东科技大学“六级模拟考，挑战英语高峰”——备战六级专题活动。联系人：刘笛15297637131",
#                  "joinType":1,"signType":1,"signPlace":"","signLong":"","signLat":"","signRadius":0,
#                  "needSignOut":1,"allowUserType":1,"allowCollege":[],"allowYear":[],"allowTribe":[],
#                  "allowBranch":[],"contact":"刘笛","contactPhone":"***********","tags":null,
#                  "signStartTime":"2024-11-23 13:30:00","signOutStartTime":"2024-11-23 17:00:00",
#                  "workUpload":0,"canVote":0,"puType":0,"status":21,
#                  "attachName":"https://img.pocketuni.net/data/uploads/2024/1117/16/06440d60-5b3e-4c43-9275-61c826df7edd.docx",
#                  "uid":208775822770176,"tid":0,"is54":0,"isZyfwActivity":0,
#                  "maxMinutes":-1,"zyfwCert":1},
#                 "userStatus":{"hasJoin":0,"hasSignIn":0,"hasSignOut":0,"hasFinish":0,"hasXinde":0},
#                 "evaluateInfo":{"averageStar":0,"praise":""},
#                 "buttonInfo":[{"name":"收藏","event":"collect"},
#                               {"name":"报名未开始","event":""}],
#                 "joinInfo":{"name":"我要参赛","event":"join"},
#                 "newsInfo":{"id":0,"title":"","content":"","createdAt":""},"voteConfig":{"status":1,"allowMultiVotes":1,"playerCanVote":1,"voteLimit":0,"voteType":0,"playerCanJoin":1,"isMember":0},"iscreator":0,"workButton":{"name":"","url":"","status":0,"reason":"","event":0},"puType":0,"joinStatus":{"name":"","cancelName":"","ruleName":"","joinStatus":0}}}

# {"key":"categorys","key2":"subCategoryId","name":"活动分类","infoList":[{"id":208776145732450,"name":"思想政治与道德修养","infoList":[]},{"id":208776145732451,"name":"社会实践与志愿服务","infoList":[]},{"id":208776145732452,"name":"文化艺术与身心发展","infoList":[]},{"id":208776145732453,"name":"学术科技与创新创业","infoList":[]},{"id":208776145732454,"name":"社会工作与技能拓展","infoList":[]}]},
# {"name":"团支部考核","short":"league","status":0},{"name":"劳动教育","short":"labor","status":0},{"name":"成果认定二级审核","short":"apply","status":0},{"name":"活动二级分类","short":"activity_sub_category","status":0},{"name":"成果认定子分类","short":"apply_sub_category","status":0},{"name":"活动心得上传","short":"activity_work_upload","status":0},
# "list":[{"key":"categorys","key2":"subCategoryId","name":"活动分类",
#          "infoList":[{"id":208776145732450,"name":"思想政治与道德修养",
#                       "infoList":[]},{"id":208776145732451,"name":"社会实践与志愿服务","infoList":[]},
#                      {"id":208776145732452,"name":"文化艺术与身心发展","infoList":[]},
#                      {"id":208776145732453,"name":"学术科技与创新创业","infoList":[]},{"id":208776145732454,"name":"社会工作与技能拓展","infoList":[]}]},
#         {"key":"oids","key2":"","name":"归属组织","infoList":[{"id":208775812284442,"name":"校团委","infoList":null},{"id":208775812284443,"name":"宣传部","infoList":null},{"id":208775812284444,"name":"学生工作处","infoList":null},{"id":208775812284445,"name":"校友工作办公室","infoList":null},{"id":208775812284446,"name":"安管处","infoList":null},{"id":208775812284447,"name":"校友办","infoList":null}]},
# {"code":0,"message":"成功",
#  "data":
#          {"baseInfo":
#                  {"name":"【能源学院】嘻笑汇相声＆表演工作坊文艺演出",
#                   "logo":"https://img.pocketuni.net/data/uploads/2024/1116/21/66a1e4b4-5c06-42b4-8f42-3ec4790e45b6.png",
#                   "creatorName":"矿业社团","creatorUID":10706945,"statusName":"未开始","categoryId":208776145732452,
#                   "categoryName":"文化艺术与身心发展",
#                   "subCategoryId":0,"levelId":0,"levelName":"",
#                   "credit":1,
#                   "puAmount":0,"baseInfo":{"name":"【计算机科学与工程学院】配音大赛决赛（观众）","logo":"https://img.pocketuni.net/data/uploads/2024/1113/21/8134d2db-0a15-4d18-978b-cde00a1e6e90.png","creatorName":"计算机学院学生会","creatorUID":10707149,"statusName":"已结束","categoryId":208776145732450,"categoryName":"思想政治与道德修养","subCategoryId":0,"levelId":0,"levelName":"","credit":1,"puAmount":0,"joinStartTime":"2024-11-14 12:00:00","joinEndTime":"2024-11-17 12:00:00","startTime":"2024-11-17 19:00:00","endTime":"2024-11-17 21:00:00","address":"大活二楼报告厅","allowUserCount":200,"joinUserCount":156,"signInUserCount":148,"signOutUserCount":145,"description":"为深入学习宣传贯彻党的二十大精神，丰富校园文化生活，让学生沉浸式感受党的光辉奋斗历程和伟大革命精神，彰显当代大学生昂扬向上的青春风采，特举办“峥嵘岁月留声，红韵经典重现”红色经典影片配音大赛。活动联系人：刘灏轩  联系方式：18562701278\n","joinType":1,"signType":1,"signPlace":"","signLong":"","signLat":"","signRadius":0,"needSignOut":1,"allowUserType":1,"allowCollege":[],"allowYear":[],"allowTribe":[],"allowBranch":[],"contact":"刘灏轩","contactPhone":"***********","tags":null,"signStartTime":"2024-11-17 18:00:00","signOutStartTime":"2024-11-17 20:30:00","workUpload":0,"canVote":0,"puType":0,"status":23,"attachName":"https://img.pocketuni.net/data/uploads/2024/1113/21/8bf809c6-7c4e-4e7e-873c-a96b15f8b6cf.docx","uid":208775875199174,"tid":0,"is54":0,"isZyfwActivity":0,"maxMinutes":-1,"zyfwCert":1},
#                   "joinStartTime":"2024-11-20 08:00:00","joinEndTime":"2024-11-23 19:00:00","startTime":"2024-11-23 19:00:00","endTime":"2024-11-23 21:00:00",
#                   "address":"大学生活动中心二楼报告厅",
#                   "allowUserCount":100,"joinUserCount":1,
#                   "signInUserCount":1,"signOutUserCount":1,"description":"随着社会的快速发展和娱乐方式的多元化，传统的语言类艺术形式逐渐在现代文化中被边缘化。然而，相声、小品、戏曲、快板、话剧等表演艺术承载着丰富的文化内涵，是中国传统文化的重要组成部分。为了更好地传承和发扬这些经典艺术形式，同时提升同学们的文化素养和艺术欣赏水平，学校决定举办“嘻笑汇相声＆表演工作坊文艺演出活动”。负责人：董正凯，联系方式：15563607085",
#                   "joinType":1,"signType":1,"signPlace":"","signLong":"","signLat":"","signRadius":0,"needSignOut":1,"allowUserType":1,"allowCollege":[],"allowYear":[],"allowTribe":[],"allowBranch":[],"contact":"董正凯","contactPhone":"***********","tags":null,
#                   "signStartTime":"2024-11-23 18:00:00","signOutStartTime":"2024-11-23 20:30:00","workUpload":0,"canVote":0,"puType":0,"status":21,"attachName":"https://img.pocketuni.net/data/uploads/2024/1116/21/726d3679-c89e-4a8f-b50f-c56753175cdf.docx","uid":208775875199160,"tid":208775961183651,"is54":0,"isZyfwActivity":0,"maxMinutes":-1,"zyfwCert":1},"userStatus":{"hasJoin":0,"hasSignIn":0,"hasSignOut":0,"hasFinish":0,"hasXinde":0},"evaluateInfo":{"averageStar":0,"praise":""},"buttonInfo":[{"name":"收藏","event":"collect"},{"name":"报名未开始","event":""}],"joinInfo":{"name":"我要参赛","event":"join"},"newsInfo":{"id":0,"title":"","content":"","createdAt":""},"voteConfig":{"status":1,"allowMultiVotes":1,"playerCanVote":1,"voteLimit":0,"voteType":0,"playerCanJoin":1,"isMember":0},"iscreator":0,"workButton":{"name":"","url":"","status":0,"reason":"","event":0},"puType":0,"joinStatus":{"name":"","cancelName":"","ruleName":"","joinStatus":0}}}


# "joinType":1,"signType":1,"signPlace":"","signLong":"","signLat":"","signRadius":0,"needSignOut":1,"allowUserType":2,"allowCollege":[],"allowYear":[],"allowTribe":[{"id":252139367038976,"name":"安全工程24-1","infoList":null}],
# 、
# "baseInfo":{"name":"【计算机科学与工程学院】配音大赛决赛（观众）",
#             "logo":"https://img.pocketuni.net/data/uploads/2024/1113/21/8134d2db-0a15-4d18-978b-cde00a1e6e90.png",
#             "creatorName":"计算机学院学生会","creatorUID":10707149,"statusName":"已结束",
#             "categoryId":208776145732450,"categoryName":"思想政治与道德修养","subCategoryId":0,"levelId":0,"levelName":"","credit":1,"puAmount":0,"joinStartTime":"2024-11-14 12:00:00","joinEndTime":"2024-11-17 12:00:00","startTime":"2024-11-17 19:00:00","endTime":"2024-11-17 21:00:00","address":"大活二楼报告厅","allowUserCount":200,"joinUserCount":156,"signInUserCount":148,"signOutUserCount":145,"description":"为深入学习宣传贯彻党的二十大精神，丰富校园文化生活，让学生沉浸式感受党的光辉奋斗历程和伟大革命精神，彰显当代大学生昂扬向上的青春风采，特举办“峥嵘岁月留声，红韵经典重现”红色经典影片配音大赛。活动联系人：刘灏轩  联系方式：18562701278\n","joinType":1,"signType":1,"signPlace":"","signLong":"","signLat":"","signRadius":0,"needSignOut":1,"allowUserType":1,"allowCollege":[],"allowYear":[],"allowTribe":[],"allowBranch":[],"contact":"刘灏轩","contactPhone":"***********","tags":null,"signStartTime":"2024-11-17 18:00:00","signOutStartTime":"2024-11-17 20:30:00","workUpload":0,"canVote":0,"puType":0,"status":23,"attachName":"https://img.pocketuni.net/data/uploads/2024/1113/21/8bf809c6-7c4e-4e7e-873c-a96b15f8b6cf.docx","uid":208775875199174,"tid":0,"is54":0,"isZyfwActivity":0,"maxMinutes":-1,"zyfwCert":1},