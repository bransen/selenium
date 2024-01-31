Test Opening Pages:
This code will open each URL in a Chrome browser, wait for 3 seconds, and then compare the expected page title with the actual one. If they match, it will print a success message. If they do not match, it will raise an assertion error. You can modify the URLs and the expected titles as per your needs.

Test Opening Links:
This code will open the URL in a Chrome browser, find all the links on the page, and make a HEAD request to each link to check if it is valid. If the response status code is 200, it means the link is working. If not, it will raise an assertion error with the broken link.
