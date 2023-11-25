import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_symptoms():
  url = "https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  adult_scrape = soup.find_all('div', class_="adult")
  child_scrape = soup.find_all('div', class_="child")
  adult_symptoms = []
  child_symptoms = []
  for s in adult_scrape[0].find_all("li"):
    adult_symptoms.append(s.get_text().strip())
  for s in child_scrape[0].find_all("li"):
    child_symptoms.append(s.get_text().strip())

  symptoms = {'adult': adult_symptoms, 'child': child_symptoms}
  return symptoms

def scrape_factors(symptom):
  symptom = symptom.lower().replace(" ", "-")
  url = "https://www.mayoclinic.org/symptom-checker/" + symptom + "/related-factors/itt-20009075"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  factors_scrape = soup.find_all('div', class_="frm_item")
  factors = {}
  for t in factors_scrape:
    subtitle = t.find("legend").get_text().strip()
    sublist = []
    for f in t.find_all("label"):
      sublist.append(f.get_text().strip())
    factors[subtitle] = sublist
  return factors

def scrape_causes(symptom, factors):
  symptom = symptom.lower().replace(" ", "-")
  url = "https://www.mayoclinic.org/symptom-checker/" + symptom + "/related-factors/itt-20009075"
  factors = factors.split(",")
  # response = requests.get(url)
  # soup = BeautifulSoup(response.content, "html.parser")

      # Initialize the WebDriver (replace 'chromedriver' with the path to your WebDriver executable)
  driver = webdriver.Chrome()

  try:

      # Open the website
      driver.get(url)
      # Iterate through the list of button texts and click each button
      for factor in factors:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), '{factor}')]")))
        ActionChains(driver).move_to_element(button).click().perform()
        

      # Find and click the submit button
      submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
      ActionChains(driver).move_to_element(submit_button).click().perform()

      # Wait for the page to load after submitting the form
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='expandable factors']")))

      # Now you can scrape data from the page
      # Modify the following line to extract the specific data you need
      print("made it 3")
      scraped_data = driver.find_elements(By.XPATH, "//div[@class='expandable factors']").text
      print("made it 4")

      # need to actually scrapae this. 
      return scraped_data

  finally:
      # Close the WebDriver
      driver.quit()
