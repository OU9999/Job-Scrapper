from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    results = []
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('tr', class_="job")
    # print(jobs)
    for job in jobs:
      job_posts=job.find_all('td',class_='company position company_and_position')
      # print(job_posts)
      for post in job_posts :
        links = post.find('a',class_="preventLink")
        link = links['href']
        title=links.find('h2')
        companys = post.find('span',class_="companyLink")
        company = companys.find('h3')
        region = post.find('div',class_="location")
        job_data = {
                    'link' : f"https://remoteok.com/remote-jobs{link}",
                    'company' : company.string ,
                    'region' : region.string ,
                    'position' : title.string
        }
        
        for each in job_data:
                    if job_data[each] != None:
                        job_data[each] = job_data[each].replace(",", " ")
                    job_data[each] = job_data[each].replace("\n", " ")
        results.append(job_data)
        
    return results
        
  else:
    print("Can't get jobs.")

react = extract_jobs("react")
print(react)

