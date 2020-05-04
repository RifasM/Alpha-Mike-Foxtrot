from selenium import webdriver
import csv
driver = webdriver.Chrome('chromedriver.exe')



details = [['Name', 'sem1', 'sem2', 'sem3', 'sem4', 'sem5']]

for i in range(66, 136):
    if 0 < i < 100:
        driver.get('https://www.vtu4u.com/results/1cr17cs0'+str(i)+'?cbse=1')
    else:
        driver.get('https://www.vtu4u.com/results/1cr17cs'+str(i)+'?cbse=1')
    try:
        name = driver.find_element_by_css_selector('.student_details').text
        sem = driver.find_elements_by_css_selector('td.ng-binding.ng-scope')
        details.append([name, sem[4].text, sem[3].text, sem[2].text, sem[1].text, sem[0].text])
        print(name, "done")
    except Exception as e:
        print(e)

try:
    with open('cse.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(details)
        csvFile.close()
except Exception as e:
    print(e)
    print(details)
