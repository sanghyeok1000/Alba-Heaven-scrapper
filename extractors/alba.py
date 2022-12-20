from requests import get
from bs4 import BeautifulSoup

def extract_alba_jobs():
    base_url = "http://www.alba.co.kr/job/list/today.asp?WsSrchKeywordWord=&hidschContainText=&hidWsearchInOut=&hidSort=&hidSortOrder=&hidSortDate=&hidListView=LIST&hidSortCnt=50&hidSortFilter=Y&hidJobKind=&hidJobKindMulti=19010000&page=1&hidSearchyn=Y&strAreaMulti=02%7C%7C%EC%A0%84%EC%B2%B4%7C%7C&schtext=&selGugun=%EC%A0%84%EC%B2%B4&lastschoolcd=&careercd=&hidCareerCD=&hidLastSchoolCD=&hidLastPayCD=&hidPayStart=&sortCnt=50"
    
    response = get(f"{base_url}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="goodsList")
        for job_section in jobs:
            job_posts = job_section.find_all("tr")
            job_tds = job_posts.find_all("td")
            job_td = job_tds[1]
            for post in job_td:
                anchors = post.find_all("a")
                anchor = anchors[0]
                link = anchor['href']
                title, location, company, pay = anchor.find_all("td", class_=" ")
                job_data = {
                    'link': "http://www.alba.co.kr/"
                    'title': title,
                    'location': location.string,
                    'company': company.string,
                    'pay': pay.string
                }
                results.append(job_data)
extract_alba_jobs()