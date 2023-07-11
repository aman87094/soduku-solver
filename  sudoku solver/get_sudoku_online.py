from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# import sudoku_solution
# from sudoku_solution import *
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the path to ChromeDriver executable
webdriver_service = Service('/Users/amankumar/Downloads/chromedriver_mac64/chromedriver')

# Set up the WebDriver instance
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
# driver = webdriver.Chrome(executable_path='/Users/amankumar/Downloads/chromedriver_mac64/chromedriver')
# print('hello1')
# Navigate to the desired page
def get_sudoku():
    driver.get("https://www.sudokuonline.io/")
    # print('hello2')

    # Retrieve the page source
    page_source = driver.page_source
    # print('hello3')
    # Close the WebDriver instance
    driver.quit()
    # print('hello4')

    # Pass the page source to BeautifulSoup for parsing
    soup = BeautifulSoup(page_source, 'html.parser')
    # print('hello5')
    # print(soup)

    # Extract the desired data using BeautifulSoup
    # For example, find all the <a> tags and print their text
    # links = soup.find_all('a')
    # for link in links:
    #     print(link.text)
    arr=[]
    for i in range(9):
        temp=[]
        for j in range (9):
            temp.append(0)
        arr.append(temp)
    # print(arr)
    sudoku=soup.find('div',id="sudoku").find_all('div',class_="cell")
    for ele in sudoku:
        # temp=ele.find('data-value')
        if(ele.attrs['data-value']==''):
            arr[int(ele.attrs['data-row'])][int(ele.attrs['data-column'])]=0
        else : 
            arr[int(ele.attrs['data-row'])][int(ele.attrs['data-column'])]=int(ele.attrs['data-value'])
        # print(ele.attrs)
        # print(ele.attrs['data-value'])
        # print()
        # break
        # print(temp)
        # for e in ele :
        #     print(e)
        # break
    # for erow in arr:
    #     print(erow)
    # print('Solution : ')
    # if solve_sudoku(arr):
    #     print_grid(arr)
    # else:
    #     print("No solution exists")
    return arr
# ans=get_sudoku()
# print(ans)
