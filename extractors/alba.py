from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_alba_jobs():
    base_url = "http://www.alba.co.kr/job/list/today.asp?WsSrchKeywordWord=&hidschContainText=&hidWsearchInOut=&hidSort=&hidSortOrder=&hidSortDate=&hidListView=LIST&hidSortCnt=50&hidSortFilter=Y&hidJobKind=&hidJobKindMulti=19010000&page=1&hidSearchyn=Y&strAreaMulti=02%7C%7C%EC%A0%84%EC%B2%B4%7C%7C&schtext=&selGugun=%EC%A0%84%EC%B2%B4&lastschoolcd=&careercd=&hidCareerCD=&hidLastSchoolCD=&hidLastPayCD=&hidPayStart=&sortCnt=50"

    response = get(base_url)
    
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="goodsList")
    for job_section in jobs:
        job_posts = job_section.find_all("tr")
        for post in job_posts:
            anchors = post.find_all("a")
            if len(anchors) != 0 :
                first_anchor = anchors[0]
                link = first_anchor['href']
                title = post.find_all("span", class_="title")
                location = post.find_all("td", class_="local")
                company = post.find_all("span", class_="company")
                pay = post.find_all("td", class_="pay")
                job_data = {
                    'link': f"http://www.alba.co.kr/{link}",
                    'title': title.string,
                    'location': location.string,
                    'company': company.string,
                    'pay': pay.string
                }
                results.append(job_data)
    return results