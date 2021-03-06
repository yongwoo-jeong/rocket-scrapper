import csv
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")

def save_to_file(jobs):
    file = open(f"로켓펀치_신입{today}.csv", mode = 'w', encoding ='UTF-8-sig')
    writer = csv.writer(file)
    writer.writerow(["회사명", "직무", "연봉/경력", "지원"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return