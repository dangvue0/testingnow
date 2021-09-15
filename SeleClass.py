from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleCall():
    def __init__(self):
        PATH = "/Users/dangvue0/Downloads/chromedriver"
        self.myBrowser = webdriver.Chrome(PATH)
        self.myBrowser.get("http://www.youtube.com")
        self.defaultwindow = self.myBrowser.current_window_handle
        print(self.defaultwindow)

    # script = """window.alert("There is ZEN ZEN ZEN")"""

    # searchbox = myBrowser.find_element_by_id("search")
    # searchbox.send_keys("Zen Zen Zen")
    #
    # searchbutn = myBrowser.find_element_by_id("search-icon-legacy")
    # searchbutn.click()
    #
    # readystate = myBrowser.execute_script("document.readyState")
    # print(readystate)
    #
    # gethtmlbody = myBrowser.find_element_by_tag_name("body").text
    # print(gethtmlbody)
    #
    # if gethtmlbody.lower().find('zen zen zen') >= 0:
    #     # myBrowser.execute_script("""window.alert("There is ZEN ZEN ZEN")""")
    #     print("There is ZEN ZEN ZEN")
    # else:
    #     print("NO ZEN ZEN ZEN")

    # i = 1
    # while i <= 6:
    #     print(i)
    #
    # i += 1

    def opennewwindowandsearch(self, searchword):
        self.myBrowser.execute_script('window.open("https://google.com")')
        self.myBrowser.switch_to.window(self.myBrowser.window_handles[-1])
        # searchspace = self.myBrowser.form[0].find_elements_by_tag_name("input")[0]

        searchspace = self.myBrowser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        )
        # searchspace = self.myBrowser.find_elements_by_tag_name("input")[5]
        print(searchspace)
        searchspace.send_keys(searchword, Keys.ENTER)

        # searchspace.send_keys(Keys.ENTER)
        # print(self.myBrowser.title)
        # iscript = 'document.getElementsByTagName("input")[0].value = \"' + searchword + '\"'
        # print(iscript)
        # self.myBrowser.execute_script(iscript)


    def closewindow(self):
        tabs = self.myBrowser.window_handles
        print(tabs.__len__())
        # reversed is need to avoid error
        for tab in reversed(tabs):
            if tab != self.defaultwindow:
                print(tab.title())
                self.myBrowser.switch_to.window(tab)
                self.myBrowser.title
                self.myBrowser.close()
            else:
                self.myBrowser.switch_to.window(tab)


        # self.myBrowser.close()

        # if tabs > 1:
        #     self.myBrowser.switch_to()

        # myBrowser.find_element_by_tag_name("input")[5].value = "1"
        # document.getElementsByTagName("input")[5].value = "TETS"




    ##working: get all text on htmlpage
    # print(myBrowser.find_element_by_xpath("/html/body").text)

    # myBrowser.close()