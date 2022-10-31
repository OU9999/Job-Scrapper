websites = [
    "google.com" ,
    "naver.com" ,
    "bc.ac.kr" ,
]

for website in websites :
    if not website.startswith("https://") :
        #print("have to fix")
        website = f"https://{website}"
        print(website)
        
print(websites) # 어째서 for문 바깥에있는건 그대로?
