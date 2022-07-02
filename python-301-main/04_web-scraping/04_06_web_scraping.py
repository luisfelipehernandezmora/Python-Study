# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.
 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


## OPTIONS FOR THE SELENIUM BROWSER
webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")  #Even if the browsing is happening headless, this is for the screenshots
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")  # Avoids to get stopped when being redirected by a webpage that have a expired certificate
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"  # REFERENCE FOR USER AGENT NAMES http://www.useragentstring.com/index.php?id=19983
options.add_argument(f"user-agent={user_agent}")  # Allows to get the source code from webpages than changed the content when scrawled in a headless mode
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

url="https://www.livesport.com/mls/standings/"
driver.get(url)
source_code = driver.page_source
equipos=[]
puntos=[]
teams=driver.find_elements_by_class_name("tableCellParticipant__image")
for team in teams:
    equipos.append(team.accessible_name)


for num_camb in range(1,15):
    #Western teams 
    num1=str(2)
    num_camb=str(num_camb)
    xpath_for_scores='//*[@id="tournament-table-tabs-and-content"]/div[3]/div[1]/div['+num1+']/div/div[2]/div['+num_camb+']/span[6]'
    score_of_the_team=driver.find_element_by_xpath(xpath_for_scores).text
    puntos.append(score_of_the_team)


for num_camb in range(1,15):
    #Eastern teams 
    num1=str(3)
    num_camb=str(num_camb)
    xpath_for_scores='//*[@id="tournament-table-tabs-and-content"]/div[3]/div[1]/div['+num1+']/div/div[2]/div['+num_camb+']/span[6]'
    score_of_the_team=driver.find_element_by_xpath(xpath_for_scores).text
    puntos.append(score_of_the_team)


stats=dict()
for i in range(0,29):
    