
import hashlib,requests,urllib.parse



def HttpPost(url,data):
    headers = {"Host": "www.soutiba.cn",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
               "Referer": "https://www.soutiba.cn/"}
    ad = requests.post(url=url,data=data,headers=headers,cookies={"cisu": "1"})
    print(ad.content)

def getMd5(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()

if __name__=="__main__":
    ti = "引用自己发表的研究成果或数据，没有详细列出有关文献出处，不属于学术不端行为。（）"
    data = {"f": 1,"desc": urllib.parse.quote(ti),"token": getMd5(ti+"salt")}
    url = "https://www.soutiba.cn/wodechati.php"
    HttpPost(url,data)
