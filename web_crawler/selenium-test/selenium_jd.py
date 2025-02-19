from lxml import etree
import time, re
from openpyxl import Workbook
from selenium import webdriver
# from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait


class HemeiSelenium():
    def __init__(self):
        # 伪装请求头
        # user_agent = UserAgent().random
        # self.headers = {'User-Agent': user_agent}
        self.wb = Workbook()
        # 定义一个工作簿名称
        self.dest_filename = '苹果信息.xlsx'
        # 激活一个表单
        self.ws1 = self.wb.active
        # 为工作表起名字
        self.ws1.title = '详情数据'
        # 添加标题
        self.ws1.append(['mac', '名字', '价格',
                         '内存', '硬盘'])

    # 获取每个课程的URL
    def getEachCourseUrl(self):
        url = 'https://study.163.com/series/1202914611.htm'
        self.driver.get(url)
        time.sleep(1)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        time.sleep(1)
        page_text = self.driver.page_source
        html = etree.HTML(page_text)
        # 每个课程的URL列表
        href = html.xpath('//*[@class="wrap m-test5-wrap f-pr f-cb"]/a/@href')
        return href

    # 获取每个课程的详细信息
    def getEachCourseDetailed(self):
        href = self.getEachCourseUrl()
        # href = ['/course/introduction/1209400837.htm']
        # print(href)
        for idx, i in enumerate(list(href)):
            # 获取课程id
            id = ''.join(re.findall('\d', i))
            # 拼接每个课程的URL完整地址
            url = f'https://study.163.com/course/introduction.htm?courseId={id}#/courseDetail?tab=1'
            # 课程URL
            print(url)
            self.driver.get(url)
            # 课时、关于我们等关键词出现了，页面就是加载完毕
            WebDriverWait(self.driver, timeout=10).until(
                lambda x: "关于我们" in self.driver.page_source
                          and "课时" in self.driver.page_source)
            # time.sleep(1)
            js = 'window.scrollTo(0, document.body.scrollHeight)'
            self.driver.execute_script(js)
            # time.sleep(1)
            page_text = self.driver.page_source
            html = etree.HTML(page_text)
            # 课程名字
            name = html.xpath('//*[@class="u-coursetitle f-fl"]/h2/span/text()')[0]
            # 多少人学过
            many_people = html.xpath('//*[@class="u-coursetitle f-fl"]/div/span[1]/text()')[0].replace('人学过', '')
            # 课程价格
            price = html.xpath('//*[@class="price"]/text()')[0].replace('¥ ', '')
            nodes = html.xpath('//*[@class="section"]')
            for node in nodes:
                # 第几课时
                class_hour = node.xpath('./span[1]/text()')[0].replace('课时', '')
                # 课程标题
                class_title = node.xpath('./span[3]/text()')[0]
                # 时长，时长有空的情况需要判断
                duration = node.xpath('./span[4]/span[1]/text()')
                duration = duration[0] if len(duration) > 0 else '无时长'
                # 时长切分成分和秒
                if duration != '无时长':
                    duration_split = duration.split(':')
                    # 时长秒数
                    duration_second = int(duration_split[0]) * 60 + int(duration_split[1])
                    content = [idx + 1, name, url, many_people, price,
                               class_hour, class_title, duration,
                               duration_second]
                    # 调用写excel方法
                    self.write_excel(content)
                    print(content, '写入excel成功')
                else:
                    duration_second = '无秒数'
                    content = [idx + 1, name, url, many_people, price,
                               class_hour, class_title, duration,
                               duration_second]
                    # 调用写excel方法
                    self.write_excel(content)
                    print(content, '写入excel成功')

    # 写excel
    def write_excel(self, content):
        # 添加数据
        self.ws1.append(content)
        # 保存文件
        self.wb.save(filename=self.dest_filename)

    # 主函数
    def main(self):
        # 开始时间
        start_time = time.time()
        # 统一获取driver
        self.driver = webdriver.Chrome()
        # 调用获取每个课程的详细信息方法
        self.getEachCourseDetailed()
        # 总耗时
        use_time = int(time.time()) - int(start_time)
        print(f'爬取总计耗时：{use_time}秒')
        # 退出
        self.driver.quit()


if __name__ == '__main__':
    wyykt = HemeiSelenium()
    wyykt.main()
