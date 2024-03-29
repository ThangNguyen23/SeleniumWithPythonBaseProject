from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory:
    def create_driver(self):
        raise NotImplementedError
    
class ChromeDriverFactory(WebDriverFactory):
    def create_driver(self):
        try:
            options = webdriver.ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service = service, options = options)
        except Exception as e:
            print(f"Your error: {e}")

class EdgeDriverFactory(WebDriverFactory):
    def create_driver(self):
        try:
            options = webdriver.EdgeOptions()
            service = EdgeService(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service = service, options = options)
        except Exception as e:
            print(f"Your error: {e}")
    
    