def save_to_file(file_name,jobs) :
    file = open(f"{file_name}.csv" , "w" , encoding="UTF-8-sig")
    file.write("Company,Position,Location,URL\n")

    for job in jobs :
        file.write(f"{job['company']},{job['position']},{job['region']},{job['link']},\n")
    file.close()