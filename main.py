from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = ['a']

driver = webdriver.Firefox()
driver.get("https://www.ig.ca/en/find-an-advisor")

searchbar = driver.find_element_by_id("FindAnAdvisor_location")

searchbar.send_keys('test')

searchbar.send_keys(Keys.CONTROL + "a")
searchbar.send_keys(Keys.DELETE)

for char in alphabet:
    searchbar.send_keys(char)

    # dataset_container = driver.find_element_by_class_name(
    #     "tt-dataset tt-dataset-locations")
    dataset_container = driver.find_element_by_css_selector(
        ".tt-dataset-locations")
    locations = dataset_container.find_elements_by_class_name(
        "tt-suggestion")

    for location in locations:
        location.click()
        driver.find_element_by_class_name("input-group-button").click()

        # get each person within that location

        results_container = driver.find_element_by_id("results-container")
        results_container.find_elements_by_css_selector(
            "div.divider:nth-child(2) > div:nth-child(1) > div:nth-child(1)")

    searchbar.send_keys(Keys.CONTROL + "a")
    searchbar.send_keys(Keys.DELETE)
