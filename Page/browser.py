from Business import BaseUtil


class Browser(BaseUtil):
    def run_search(self):
        return self.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="搜索框"]').click()

    def search_input(self, search_value):
        return self.by_link_text('搜索或输入网址').send_keys(search_value)

    def search_btn(self):
        return self.by_xpath("//android.widget.TextView[@text='搜索']")
