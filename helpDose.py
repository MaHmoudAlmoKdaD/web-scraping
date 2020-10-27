# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
import time
from bs4 import BeautifulSoup
import requests

# driver.execute_script("window.open('%s', '_blank')" % dep_array[2])
main_page = requests.get('https://www.helpdose.com')
soup = BeautifulSoup(main_page.content, 'html.parser')
# get array of departments
departments = soup.find_all(class_='dropdown-item')
dep_array = []
domain = int(len(departments)/2)
for i in range(domain):
    href = departments[i]['href']
    dep_array.append(href)
# for nav in dep_array:
#     print(nav)


# get array of experts
i = 0
array_of_experts = []
for dep in dep_array:
    i=i+1
    page = requests.get(dep)
    soup = BeautifulSoup(page.content, 'html.parser')
    navs = soup.find_all(class_='btn btn-block border-radius-expert-btn p-2')
    
    for nav in navs:
        href = nav['href']
        array_of_experts.append(href)
    print('----- department'+str(i)+' Finshed -----')
# for href in array_of_experts:
#     print(href)


# get to about each expert

file = open('HelpDose.txt', 'a') 
print("File Is Creating.....")
for expert in array_of_experts:
    page = requests.get(expert)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find(class_='mb-0 mt-md-0 mt-n3').get_text()
    about_word = soup.find(class_='text-md').get_text()
    about = soup.find(class_='text-justify').get_text()
    print(expert)
    try:
        file.write(name.strip())
        file.write(about_word.strip())
        file.write(about.strip())
    except:
        print("there is exception here")
    file.write("------------------------------------------------------------------------------")
print("DONE, Thank you to Use Mahmoud Code")
