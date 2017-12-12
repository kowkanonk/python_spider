import urllib.request
import re
import os

# response = urllib.request.urlopen("https://mm.taobao.com/json/request_top_list.htm?page=1")
#html = response.read()
#print(html)
print("retriving content...")


class SpiderW:

    def getContents(self,site,path):
        pattern = re.compile('<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>',re.S)
        response = urllib.request.urlopen(site)
        page = response.read().decode('gbk')
        items = re.findall(pattern, page)
        self.makedir(path)
        for i in range(0,len(items)):
            self.saveImage(items[i][0],items[i][1],path)

    def saveImage(self,imageUrl,fileName,path):
        u = urllib.request.urlopen('https:' + imageUrl)
        data = u.read()
        f = open(path + fileName + '.jpg','wb')
        f.write(data)
        f.close()

    def makedir(self,path):
        p = path.strip()
        isExists = os.path.exists(p)
        if not isExists:
            os.makedirs(p)
            return True
        else:
            return False

spider = SpiderW()
spider.getContents('https://mm.taobao.com/json/request_top_list.htm?page=1','./picture/')
