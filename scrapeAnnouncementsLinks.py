from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

announcements_links = []

for i in range(1, 3):  # because the number of pages is 2
    driver.get('https://www.mubawab.ma/fr/pl/casablanca/listing-promotion:p:{}'.format(i))

    for element in driver.find_elements(By.XPATH, "//ul[@class='ulListing']/li"):
        announcements_links.append(element.get_attribute('linkref'))

# Create a dictionary
dict = {
    'Announcements Links': announcements_links,
}

# Assign the dictionary to a dataframe
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.transpose()

print(df)

# df.to_csv("./AnnouncementsLinks.csv", sep=',', index=False)
