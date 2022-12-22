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
            except_empty_list = []
            if anchors == []:
                pass
            else:
                except_empty_list.append(anchors)
            for anchor in except_empty_list:
                first_anchor = anchor[0]
                link = first_anchor['href']
                location = anchor.find("td", class_="local.first")
                title = anchor.find("span", class_="title")
                company = anchor.find("span", class_="company")
                pay = anchor.find("td", class_="pay")
                job_data = {
                    'link': f"http://www.alba.co.kr/{link}",
                    'title': title.string.replace(",", " "),
                    'location': location.text.replace(",", " "),
                    'company': company.string.replace(",", " "),
                    'pay': pay.string.replace(",", " ")
                }
                results.append(job_data)
    return results
print(extract_alba_jobs())