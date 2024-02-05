from selenium import webdriver
import sys

Currency_Abbr = {       # Dict for Country name reference
    'QAR':'阿联酋迪拉姆', 'AUD':'澳大利亚元', 'BRL':'巴西里亚尔', 'CAD':'加拿大元', 'CHF':'瑞士法郎', 'DKK':'丹麦克朗', 
    'EUR':'欧元', 'GBP':'英镑', 'HKD':'港币', 'IDR':'印尼卢比', 'INR':'印度卢比', 'JPY':'日元', 'KRW':'韩国元', 
    'MOP':'澳门元', 'MYR':'林吉特','NOK':'挪威克朗', 'NZD':'新西兰元', 'PHP':'菲律宾比索', 'SUR':'卢布', 'SAR':'沙特里亚尔', 
    'SEK':'瑞典克朗', 'SGD':'新加坡元', 'THP':'泰国铢', 'TRY':'土耳其里拉', 'TWD':'新台币', 'USD':'美元', 'ZAR':'南非兰特'}


def get_foreign_exchange_rate(date, currency_code):
    if currency_code in Currency_Abbr:
        Country_name = Currency_Abbr[currency_code]         # Find the corresponding country name
    else:
        print('The currency code is wrong.')                # report error if the currency code is wrong
        return 0
    
    driver = webdriver.Firefox()                        # Initialize WebDriver
    driver.get("https://www.boc.cn/sourcedb/whpj/")     # Open the website

    data = str(date)
    if len(data) == 8:
        date_str = data[:4] + '-' + data[4:6] + '-' + data[6:]      # Define the date structure
    else:
        print('The input data is wrong.')                # report error if the currency code is wrong
        return 0
      
    try:
        driver.find_element("xpath",'/html/body/div/div[5]/div[1]/div[2]/div/form/div/table/tbody/tr/td[2]/div/input').send_keys(date_str)      # Fill the start date in the blank
        driver.find_element("xpath",'/html/body/div/div[5]/div[1]/div[2]/div/form/div/table/tbody/tr/td[4]/div/input').send_keys(date_str)      # Fill the end date in the blank
        driver.find_element("xpath",'/html/body/div/div[5]/div[1]/div[2]/div/form/div/table/tbody/tr/td[6]/select').send_keys(Country_name)     # Fill the Country name in the blank
        driver.find_element("xpath",'/html/body/div/div[5]/div[1]/div[2]/div/form/div/table/tbody/tr/td[7]/input').click()                      # Click the button to search

        Price = driver.find_element("xpath", "/html/body/div/div[4]/table/tbody/tr[2]/td[4]")      # Find foreign exchange rate
        if Price.text == '':        # If there is no corresponding foreign exchange rate, return None
            with open('result.txt', 'w') as file:      # Print the data into a txt file
                file.write('未查询到' + Country_name + '的现汇卖出价')
            return None
        else:
            with open('result.txt', 'w') as file:      # Print the data into a txt file
                file.write(Country_name + '在' + date_str + '的现汇卖出价：' + Price.text)
            return Price.text
    finally:
        driver.quit()       # Quit the drive

# Test:
print(get_foreign_exchange_rate(sys.argv[1], sys.argv[2]))