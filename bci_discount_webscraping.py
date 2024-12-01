from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import discounts_library as dl

def GetCardWrap(card_data : list) -> list:
    """
    Pulls the discount info for all available cards in a page; then adds them to a list.
    
    Parameters:
    card_data (list): A list containing the previous information given.
    
    Returns:
    list: The updated list with added data.
    """
    dl.waitforme(3.5)
    card_wrap = driver.find_element(By.XPATH, '//div[@class="w-100 pl-lg-4 d-flex flex-wrap d-md-block"]')
    
    html_cards = card_wrap.get_attribute("innerHTML")
    soup = BeautifulSoup(html_cards, 'html.parser')
        
    all_cards = soup.find_all('div', class_="carrousel__item d-inline-block mb-4")
    for card in all_cards:
        try:
            card_image_url = card.find('img', class_="card-img__logo shadow-normal").attrs['src']
        except:
            card_image_url = None
        card_title = card.find('p', class_="card__title color-gray-dark font-weight-bold mb-3 text-truncate-2").text.strip()
        card_description = card.find('p', class_="card__text mb-4 text-truncate-2").text
        card_url = card.find('a', class_="sub-text btn btn-link-light text-uppercase").attrs['href']        
        card_tuple = (card_title, card_description, card_image_url, card_url)
        card_data.append(card_tuple)
    return card_data

    
if __name__ == "__main__":
    # Chromium : C:\Program Files (x86)\chrome-win64\chrome.exe
    options = Options()
    options.add_experimental_option(name="detach", value=True)
    path = "C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.bci.cl/beneficios/beneficios-bci/todas'
    driver.get(url)
    driver.maximize_window()

    card_data = []
    GetCardWrap(card_data)
    
    while True:
        # print("checking the next page button")
        nextpagebutton = driver.find_element(By.XPATH, '//button[@aria-label="next page button"]')
        
        if nextpagebutton.get_attribute("disabled") == None:
            nextpagebutton_available = True
            # print(f'is the next page available? : {nextpagebutton_available}')
        else:
            nextpagebutton_available = False
            # print(f'is the next page available? : {nextpagebutton_available}')
            
        if nextpagebutton_available == True:
                # print("changing pages")
                driver.execute_script('arguments[0].click()', nextpagebutton)
                card_data = GetCardWrap(card_data)    
        else:
            # print("stopped collecting info")
            break

    with open('Py\\Utility\\discount_compiler\\bci.txt', 'w', encoding='utf-8') as text:
        for card in card_data:
            text.write(f'{card[0]}\n\n\t{card[1]}\n\tLOGO: {card[2]}\n\tURL: {card[3]}\n\n')
    text.close()