# %%
# Prerequisite required
#    1. Python3
#    2. Library BeautifulSoup for parsing HTML and XML documents 
#            Command on cmd: pip install beautifulsoup4
#    3. For this program, home.html in same directory
#    4. Library lxml for processing XML and HTML in the Python language.
#            Command on cmd: pip install lxml

# %%
from bs4 import BeautifulSoup

# %%
with open('home.html',mode='r') as html_file:
    # Raw content output
    content = html_file.read()
    # print(content)

    # Raw content output with beautification for better understanding/visualization
    soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())

# %%
    # To get course name only
    tags = soup.find_all("h5")
    print("Tags output of Course name from local webpage home.html")
    for i in tags:
        print(i.text)

# %%
    # To get course list and its respective course prices
    course_cards = soup.find_all('div',class_='card')
    print("\nCourse along with its course fee")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(' ')[-1]
        print(f"{course_name} cost {course_price}")
        

# %%


# %%
