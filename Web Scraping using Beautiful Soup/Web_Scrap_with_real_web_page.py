# %%
# Prerequisites
    # 1. Python3
    # 2. Library requests for making HTTP requests.
    #         Command on cmd: pip install requests
    # 3. Library BeautifulSoup for parsing HTML and XML documents 
    #         Command on cmd: pip install beautifulsoup4
    # 4. For this program, create empty posts directory to save output files into it
    # 5. Library time, to use sleep function to regenrate output untill user interruption

# %%
"""
#### Program to execute Jobs at Delhi for Python technology using BeautifulSoup
"""

# %%
from bs4 import BeautifulSoup
import requests
import time

# %%
def find_jobs():
    # Store link into html_text variable
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=Delhi").text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace('  ','')
            skills = job.find('span', class_="srp-skills").text.replace('  ','')
            more_info = job.header.h2.a['href']

            # Write output directly into .txt file format
            with open(f"./posts/{index}.txt",'w') as file:
                file.write(f"Company: {company_name.strip()}\n")
                file.write(f"Required skills: {skills.strip()}\n")
                file.write(f"More info: {more_info}\n")
            print(f'File saved: {index}')

# %%
if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait = 2 # 5 minutes of wait to get updated jobs
        print(f'Waiting for {time_wait} minutes...')
        time.sleep(time_wait*60)
        