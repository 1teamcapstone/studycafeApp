import time
import csv

from os import times
from typing import ClassVar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 이벤트 호출 후 약간의 시간(ex. 클릭 이벤트 후 페이지 변경에 소비되는 시간)
tick = 0.3
# 검색어
searchWord = "용인 스터디카페"

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://map.kakao.com/")

elem = driver.find_element(By.NAME, "q")
elem.send_keys(searchWord)
elem.send_keys(Keys.RETURN)

place_tap = driver.find_element(By.CLASS_NAME, "option1")
driver.execute_script("arguments[0].click();", place_tap)

time.sleep(tick)

def parse(): 
    # CSV 준비
    f = open(searchWord+'.csv', 'a', newline='')
    wr = csv.writer(f)

    global count
    places = driver.find_elements(By.CSS_SELECTOR, "ul.placelist > li.PlaceItem")
    # print(len(places))
    for place in places:
        name = place.find_element(By.CLASS_NAME, "link_name")
        # print("상 호 명: " + name.text)
        category = place.find_element(By.CLASS_NAME, "subcategory")
        # print("카테고리: " + category.text)
        address = place.find_element(By.CSS_SELECTOR, "div.info_item > div.addr > p")
        # print("주    소: " + addr.text)
        rating = place.find_element(By.CSS_SELECTOR, "div.rating > span.score > em")
        # print("별점: " + rating.text)
        reviews = place.find_element(By.CSS_SELECTOR, "div.rating > a.review > em")
        # print("리뷰개수: " + reviews.text)
        time = place.find_element(By.CSS_SELECTOR, "div.openhour > p.periodWarp > a")
        # print("운영시간: " + time.text)
        phone = place.find_element(By.CSS_SELECTOR, "div.info_item > div.contact > span.phone")
        # print("전화번호: " + phone.text)
        count += 1
        # CSV 작성   
        wr.writerow([count, name.text, category.text, address.text, rating.text, reviews.text, time.text, phone.text]) 
    f.close()

max_cnt = driver.find_element(By.ID, "info.search.place.cnt").text
print("전체개수: " + max_cnt)
# 파싱한 가게 수
count = 0

# 다음 페이지가 있는가?
page_div = driver.find_element(By.ID,"info.search.page")
hiddenPage = page_div.get_attribute('class').find("HIDDEN")

# 페이지가 여러 개인 경우
if(hiddenPage == -1):
    # 전체 상점을 찾을 때 까지 반복
    while(int(max_cnt) > count):
        pages = page_div.find_elements(By.CSS_SELECTOR, "div.pageWrap > a")
        # print(len(pages))
        for page in pages:
            # 숨겨지지 않은 번호 클릭
            if(page.get_attribute('class').find('HIDDEN') == -1):
                driver.execute_script("arguments[0].click();", page)
                time.sleep(tick)
                try:
                    parse()
                except:
                    print("\n\t\t검색 결과가 없습니다.")
                time.sleep(tick)

        # 5페이지 넘기기
        next_btn = page_div.find_element(By.CSS_SELECTOR, "div.pageWrap > button.next")
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(tick)

# 페이지가 하나 뿐인 경우            
else:
    try:
        parse()
    except:
        print("\n\t\t검색 결과가 없습니다.")

print("total: " + str(count))

# 코드 실행 후 브라우저 종료를 희망할 경우 아래 주석을 제거
# driver.close()