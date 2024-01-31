from selenium import webdriver
import time

# Create a ChromeDriver instance
driver = webdriver.Chrome(r'D:\chromedriver')

# Define the URLs to test
urls = ["https://www.python.org", "https://www.selenium.dev", "https://realpython.com"]

# Loop through the URLs and test each one
for url in urls:
    # Open the URL
    driver.get(url)
    # Wait for 3 seconds
    time.sleep(3)
    # Check if the page title matches the expected one
    expected_title = driver.title
    actual_title = driver.execute_script("return document.title")
    assert expected_title == actual_title, f"Page title for {url} did not match"
    # Print a success message
    print(f"Page title for {url} matched")

# Close the browser
driver.quit()