import requests
import argparse
from Lib import Head
from concurrent.futures import ThreadPoolExecutor


def get_information(url,byte_size,out_file):
    # 判断状态响应码不等于404 并且 文件大于或等于xxx字节
    if Head.get_status_code(url) != requests.codes.not_found and Head.get_file_size(url=url) >= byte_size:
        with open(out_file,"a",encoding="utf-8") as res:
            result = url + "\t" + Head.get_file_type(url) + "\t" + Head.get_service_name(url)
            print(result)
            res.write(url+"\n")
            res.close()
    else:
        pass

def shell():
    # 线程参数
    # 指定字典
    # 指定文件
    # 指定文件字节大小
    # 指定导出文件
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file",type=str,help="指定扫描文件")
    parser.add_argument("-o","--outfile",type=str,default="./result.txt",help="导出文件")
    parser.add_argument("-t",type=int,default=10,help="指定线程数,默认10")
    parser.add_argument("-D","--Dic",type=str,default="./Dic/dict.txt",help="指定字典文件,默认dict.txt")
    parser.add_argument("-size",type=int,default=3500000,help="指定文件字节大小,默认3500000(用于过滤误报)")
    args = parser.parse_args()
    return args

def main():
    print('''
       ___             __                   ___                        
      |_ _|  _ _      / _|  ___      o O O / __|   __    __ _   _ _    
       | |  | ' \    |  _| / _ \    o      \__ \  / _|  / _` | | ' \   
      |___| |_||_|  _|_|_  \___/   TS__[O] |___/  \__|_ \__,_| |_||_|  
    _|"""""||"""""||"""""||"""""| {======||"""""||"""""||"""""||"""""| 
    "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
                        
                                                --作者:tutu
                                                --声明:仅供学习,禁止用于非法活动!
''')
    file_name = shell().file
    payload_dic = shell().Dic
    file_size = shell().size
    out_file = shell().outfile
    task = shell().t
    if file_name == None:
        print("[-] 请指定扫描文件")
    else:
        # 开启线程池 后续可设计成交互式
        pool = ThreadPoolExecutor(task)
        with open(file_name, "r", encoding="utf-8") as urls:
            print("Url: \t\t\t File-Type: \t\t\t Server-name:")
            # 第一层遍历域名
            for url in urls:
                domain = url.replace("\n", "").replace("/", "").replace("https:", "").replace("http:", "")
                with open(payload_dic, "r", encoding="utf-8") as dic:
                    # 第二层拼接Payload
                    for catalogue in dic:
                        # #domian#替换成当前域名进行测试
                        payload = "http://" + domain + "/" + catalogue.replace("*domain*", domain).replace("\n", "")
                        # print(payload)
                        future = pool.submit(get_information, payload,file_size,out_file)


if __name__ == '__main__':
    main()
