from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonUtilities:
    def __init__(self, driver, ui_hash_map):
        self.driver = driver
        self.ui_hash_map = ui_hash_map

    def wait_for_element(self, element_hash_map, retries=10):
        for i in range(retries):
            try:
                element = self.find_element(element_hash_map)
                break
            except Exception as element_found_exception:
                if i + 1 == retries:
                    raise element_found_exception
        return element

    def find_element(self, element_hash_map):
        element_timeout = 10
        if 'locator' in element_hash_map:
            cmd = element_hash_map['locator']
            element = self.driver.find_element_by_android_uiautomator(cmd)
        else:
            element = WebDriverWait(self.driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, element_hash_map["resource_id"]))
            )
        return element

    def click(self, element):
        element.click()
