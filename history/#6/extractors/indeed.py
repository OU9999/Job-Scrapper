from ast import arg
from tkinter import ANCHOR
from selenium import webdriver
from bs4 import BeautifulSoup


def get_page_count(keyword) :
    browser = webdriver.Chrome()

    base_url = "https://kr.indeed.com/jobs?q="

    browser.get(f"{base_url}{keyword}")
    # soup = BeautifulSoup(browser.page_source, "html.parser")
    # # pagination=soup.find("ul", class_="pagination-list")
    # pagination = soup.find("nav")
    
    # if pagination == None :
    #     return 1
    # # pages=pagination.find_all("li",recursive=False)
    # pages = pagination.select("div")
    # count = len(pages)
    # if count >= 5 :
    #     return 5
    # else :
    #     return count
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        pagination = soup.find("nav")
        if pagination == None:
            return 1
        else:
            pages = pagination("div")
            count = len(pages)
            if count >= 5:
                return 5
            else:
                return count
    else:
        pages = pagination.find_all("li", recursive=False)
        count = len(pages)
        if count >= 5:
            return 5
        else:
            return count

def extract_idd_jobs(keyword) :
    pages = get_page_count(keyword)
    print("Found",pages,"pages")
    results = []
    for page in range(pages) :
        browser = webdriver.Chrome()
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting :", final_url)
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        if job_list != None :
            jobs = job_list.find_all('li', recursive=False) # 바로 밑에있는것들만 찾기
            for job in jobs :
                zone = job.find("div", class_="mosaic-zone")
                if zone == None :
                    anchor = job.select_one("h2 a")
                    title = anchor['aria-label']
                    link = anchor['href']
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        'link' : f"https://kr.indeed.com{link}",
                        'company' : company.string ,
                        'region' : location.string ,
                        'position' : title
                    }
                    for each in job_data:
                        if job_data[each] != None:
                           job_data[each] = job_data[each].replace(",", " ")
                    results.append(job_data)
    return results
            