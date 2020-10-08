from selenium import webdriver

game = input('Enter the name of a steam game: ')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)
driver.get('https://store.steampowered.com/')

search_box = driver.find_element_by_xpath('//*[@id="store_nav_search_term"]')
search_box.send_keys(game)
search_button = driver.find_element_by_xpath('//*[@id="store_search_link"]/img')
search_button.click()
result_button = driver.find_element_by_xpath('//*[@id="search_resultsRows"]/a[1]')
result_button.click()

price = driver.find_element_by_class_name('game_purchase_price.price')
price_text = price.text
print(price_text)


