import requests
import urllib3
from fake_useragent import UserAgent

# 忽略https ssl报错
urllib3.disable_warnings(0)
# 随机UA
ua = UserAgent()
headers = {'User-Agent': ua.random}

def get_file_size(url):
    # 通过字节流去获取文件大小
    try:
        res = requests.get(url=url, headers=headers, timeout=3,stream=True)
        Content_length = res.headers.get("Content-length")
        return int(Content_length)
    except Exception as infoError:
        # print("[-]",infoError)
        pass

def get_status_code(url):
    # 返回状态响应码
    try:
        Status_Code = requests.get(url=url, headers=headers, timeout=3, stream=True).status_code
        return Status_Code
    except Exception as StatusErr:
        # print("[-]",StatusErr)
        pass

def get_service_name(url):
    # 返回中间件类型
    try:
        res = requests.get(url=url, headers=headers, timeout=3, stream=True)
        Server_name = res.headers.get("Server")
        return Server_name
    except Exception as ServerErr:
        # print("[-]",ServerErr)
        pass

def get_file_type(url):
    # 返回文件类型
    try:
        res = requests.get(url=url, headers=headers, timeout=3, stream=True)
        File_Type = res.headers.get("Content-Type")
        return File_Type
    except Exception as TypeErr:
        # print("[-]",TypeErr)
        pass
