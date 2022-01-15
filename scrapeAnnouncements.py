from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# import csv file "AnnouncementsLinks.csv"
df = pd.read_csv('AnnouncementsLinks.csv')

# Launch the webdriver
driver = webdriver.Chrome()
# driver.get('https://www.mubawab.ma/fr/p/2755/paradise-beach')

# lists to use to append our scraped elements
project_name = []
place = []
price = []
standing = []
state = []
delivery = []
advertiser = []
advertiser_phone = []
longitude = []
latitude = []

# Looping over the links scraped before
for i in range(len(df)):
    url = (df['Announcements Links'].iloc[i])
    driver.get(url)

    # Scrape project name
    for proj_name in driver.find_elements(By.XPATH, "//h1[@class='SpremiumH2']"):
        project_name.append(proj_name.text)

    # Scrape the place of the project
    for plc in driver.find_elements(By.XPATH, "//span[@class='immoDetails vAlignM darkblue']"):
        place.append(plc.text)

    # Scrape the longitude of the place
    for long in driver.find_elements(By.XPATH, "//div[@id='mapOpen']"):
        longitude.append(long.get_attribute('lon'))

    # Scrape the latitude of the place
    for latit in driver.find_elements(By.XPATH, "//div[@id='mapOpen']"):
        latitude.append(latit.get_attribute('lat'))

    # Scrape the price
    for prc in driver.find_elements(By.XPATH, "//div[@class='promotionInfoBox col-3']"):
        price.append(prc.text)

    # Scrape the standing
    for stnding in driver.find_elements(By.CSS_SELECTOR, ".icon-award~ .immoBadge"):
        standing.append(stnding.text)

    # Scrape the state
    for stt in driver.find_elements(By.CSS_SELECTOR, ".icon-wrench~ .immoBadge"):
        state.append(stt.text)

    # Scrape the delivery
    for dlivry in driver.find_elements(By.CSS_SELECTOR, ".icon-key~ .immoBadge"):
        delivery.append(dlivry.text)

    # Scrape the advertiser
    for advrts in driver.find_elements(By.XPATH, "//h2[@class='agencyBoxH2']"):
        advertiser.append(advrts.text)

    # Scrape the advertiser phone
    for advrts_phone in driver.find_elements(By.CSS_SELECTOR, ".icon-phone+ span"):
        advertiser_phone.append(advrts_phone.text)


# Create a dictionary that contain all the elements scraped
dict = {
    'Project Name': project_name,
    'Place': place,
    'Longitude': longitude,
    'Latitude': latitude,
    'Price': price,
    'Standing': standing,
    'State': state,
    'Delivery': delivery,
    'Advertiser': advertiser,
    'Advertiser Phone': advertiser_phone
}

# Assign to dataframe
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.transpose()

print(df)

#df.to_csv("./Announcements.csv", sep=',', index=False)
