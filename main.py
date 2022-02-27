#import uptimerobot
import os
import webserver
webserver.awake(f"https://{os.environ['REPL_SLUG']}.{os.environ['REPL_OWNER']}.repl.co")
try:
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
except ImportError:
  os.system('pip install selenium')
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--FontRenderHinting[none]")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.get(f"https://{os.environ['REPL_SLUG']}.{os.environ['REPL_OWNER']}.repl.co")
driver.get_screenshot_as_file("pain.png")