from appium import webdriver


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_title(self):
        return self.driver.title