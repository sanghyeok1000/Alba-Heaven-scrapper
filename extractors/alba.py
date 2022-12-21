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
            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[0]
                link = anchor['href']
                title = post.find("span", class_="title")
                location = post.find("td", class_="local")
                company = post.find("span", class_="company")
                pay = post.find("td", class_="pay")
                job_data = {
                    'link': f"http://www.alba.co.kr/{link}",
                    'title': title.string,
                    'location': location.string,
                    'company': company.string,
                    'pay': pay.string
                }
                results.append(job_data)
        return results