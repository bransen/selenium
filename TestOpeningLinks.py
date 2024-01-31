from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Create a ChromeDriver instance
driver = webdriver.Chrome()

# Define the URL to test
url = "https://www.python.org"

# Open the URL
driver.get(url)

# Find all the links on the page
links = driver.find_elements (By.TAG_NAME, "a")

# Loop through the links and check if they are valid
for link in links:
    # Get the href attribute of the link
    href = link.get_attribute("href")
    # Make a HEAD request to the link
    response = requests.head(href)
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Broken link: {href}"

# Close the browser
driver.quit()