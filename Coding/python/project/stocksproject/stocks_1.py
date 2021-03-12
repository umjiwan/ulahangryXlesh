import requests
from bs4 import BeautifulSoup
import time
import datetime
url = "https://finance.naver.com/item/main.nhn?code=005930"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

while True:
#close 종가(전일)
    td_first = bs_obj.find("td", {"class": "first"}) # 태그 td, 속성값 first 찾기
    blind = td_first.find("span", {"class": "blind"}) # 태그 span, 속성값 blind 찾기
    close = blind.text


#현재가
    
# high 고가
    table = bs_obj.find("table", {"class": "no_info"}) # 태그 table, 속성값 no_info 찾기
    trs = table.find_all("tr") # tr을 list로 []
    first_tr = trs[0] # 첫 번째 tr 지정
    tds = first_tr.find_all("td") # 첫 번째 tr 안에서 td를 list로
    second_tds = tds[1] # 두 번째 td 지정
    high = second_tds.find("span", {"class": "blind"}).text

# open 시가
    second_tr = trs[1] # 두 번째 tr 지정
    tds_second_tr = second_tr.find_all("td") # 두 번째 tr 안에서 td를 list로
    first_td_in_second_tr = tds_second_tr[0] # 첫 번째 td 지정
    open = first_td_in_second_tr.find("span", {"class": "blind"}).text

# low 저가
    second_td_in_second_tr = tds_second_tr[1] # 두 번째 td 지정
    low = second_td_in_second_tr.find("span", {"class": "blind"}).text
    
    now = datetime.datetime.now()    
    







    print("")
    print("")
    print("")
    print("")
    print("")
    print("-------------------------")
    print(f"측정시간 : {now}")
    print("-------------------------")
    print(f"전날종가 : {close}원")
    print(f"고가 : {high}원")
    print(f"시가 : {open}원")
    print(f"저가 : {low}원")
    print("-------------------------")
    print("")
    print("")
    print("")
    print("")
    print("")


    time.sleep(0.5)
