from unittest import result
from requests import get

websites = [
    "google.com" ,
    "https://naver.com" ,
    "bc.ac.kr" ,
]

results = {}
for website in websites :
    if not website.startswith("https://") :
        #print("have to fix")
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200 :
        results[website] = "OK"
    else :
        results[website] = "NOT OK"

print(results)