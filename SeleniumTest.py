from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/Users/dangvue0/Downloads/chromedriver"
myBrowser = webdriver.Chrome(PATH)
myBrowser.get("http://www.youtube.com")
print(myBrowser.title)

# script = """window.alert("There is ZEN ZEN ZEN")"""

searchbox = myBrowser.find_element_by_id("search")
searchbox.send_keys("Zen Zen Zen")

searchbutn = myBrowser.find_element_by_id("search-icon-legacy")
searchbutn.click()

readystate = myBrowser.execute_script("document.readyState")
print(readystate)

gethtmlbody = myBrowser.find_element_by_tag_name("body").text
# print(gethtmlbody)

if gethtmlbody.lower().find('zen zen zen') >= 0:
    # myBrowser.execute_script("""window.alert("There is ZEN ZEN ZEN")""")
    print("There is ZEN ZEN ZEN")
else:
    print("NO ZEN ZEN ZEN")

i = 1
while i <= 6:
    print(i)
    myBrowser.execute_script('window.open("https://google.com")')
    myBrowser.switch_to.window(myBrowser.window_handles[-1])
    print(myBrowser.title)
    iscript = 'document.getElementsByTagName("input")[5].value = \"' + str(i) + '\"'
    print(iscript)
    myBrowser.execute_script(iscript)
    i += 1

    # myBrowser.find_element_by_tag_name("input")[5].value = "1"
    # document.getElementsByTagName("input")[5].value = "TETS"




##working: get all text on htmlpage
# print(myBrowser.find_element_by_xpath("/html/body").text)

# myBrowser.close()