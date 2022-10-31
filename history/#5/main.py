from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_idd_jobs

def looking_good() :
    print()
    print("//"*75)
    print()
    
keyword = input("What do yo want search for? : ")

wwr = extract_wwr_jobs(keyword)
idd = extract_idd_jobs(keyword)
jobs = wwr + idd

file = open(f"{keyword}.csv" , "w" , encoding="UTF-8-sig")
file.write("Company,Position,Location,URL\n")

for job in jobs :
    file.write(f"{job['company']},{job['position']},{job['region']},{job['link']},\n")
file.close()