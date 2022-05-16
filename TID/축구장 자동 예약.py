import calendar

from selenium import webdriver
import datetime
import sys
import os

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(os.getcwd() + '/files/chromedriver', options=options)
driver.implicitly_wait(3)


def get_sunday(year, month):
    sunday_list = []
    result = calendar.monthcalendar(year, month)
    for week in result:
        if week[6]:
            sunday_list.append(week[6])

    return sunday_list

def reservation(email, password):
    login_url = 'https://sports.gangseo.seoul.kr/fmcs/43?referer=https%3A%2F%2Fsports.gangseo.seoul.kr%2Ffmcs%2F5'
    driver.get(login_url)

    driver.find_element_by_id('user_id').send_keys(email)
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_xpath("//button[contains(text(), '로그인')]").click()

    year = f'{(datetime.datetime.now() + datetime.timedelta(days=35)).year}'
    month = f'{(datetime.datetime.now() + datetime.timedelta(days=35)).month}'
    sunday_list = get_sunday(int(year), int(month))
    month = month.zfill(2)

    place_info = {'축구장': 1, '풋살장 A': 2, '풋살장 B': 3}
    has_soccer = False
    has_reserve = False

    for day in sunday_list:
        for place_name, place_id in place_info.items():
            if has_reserve:
                has_reserve = False
                break
            if has_soccer and place_name == '축구장':
                continue
            try:
                day = str(day).zfill(2)
                url = f'https://sports.gangseo.seoul.kr/fmcs/28?facilities_type=T&base_date={year}{month}{day}&rent_type=1001&center=GANGSEO01&part={"02" if place_id == 1 else "03"}&place={place_id}#regist_list'
                driver.get(url)
                try:
                    driver.find_element_by_id('checkbox_time_4').click()
                    reserve_time = '14-16'
                except:
                    reserve_time = '16-18'
                    driver.find_element_by_id('checkbox_time_5').click()
                driver.find_element_by_xpath("//button[contains(text(), '대관신청')]").click()
                driver.find_element_by_id('users').send_keys('22' if place_name == '축구장' else '15')
                driver.find_element_by_id('purpose').send_keys('축구' if place_name == '축구장' else '풋살')
                driver.find_element_by_id('agree_use1').click()
                driver.find_element_by_xpath(
                    '/html/body/div[2]/div[2]/div/div[2]/section/div/article/div/div/form/fieldset/p[2]/button').click()
                print(f'{year}-{month}-{day} | {place_name} {reserve_time} 예약 성공')
                has_soccer = True if place_name == '축구장' else False
                has_reserve = True
            except:
                print(f'{year}-{month}-{day} | {place_name} 예약 실패')

email = sys.argv[1]
password = sys.argv[2]

reservation(email, password)
