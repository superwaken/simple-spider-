# 此应用是基于requests模块的简单爬去百度贴吧数据的功能


import requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input("贴吧名称")
        self.start_paga = int(input("输入开始页"))
        self.end_page = int(input("输入结束页"))
        self.base_url = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self, url, params):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
        return data

    # 数据写入文件
    def wirte_file(self, data, page):
        file_path = "Tieba/" + str(page) + "页.html"
        print("正在抓取{}页的数据".format(page))
        with open(file_path, "w") as f:
            f.write(data)
        print("数据写入成功！")

    # 程序调度
    def run(self):
        for page in range(self.start_paga, self.end_page+1):
            params = {
                "kw": self.tieba_name,
                "pn": (page-1)*50
            }
            # 发送请求
            data = self.send_request(self.base_url, params=params)

            # 保存
            self.wirte_file(data, page)

if __name__ == '__main__':
     spider = TiebaSpider()
     spider.run()