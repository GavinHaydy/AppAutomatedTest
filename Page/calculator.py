from Business.BaseUtil import BasePage


class Browser(BasePage):
    def one(self):
        self.by_id('com.miui.calculator:id/btn_1_s').click()

    def two(self):
        self.by_id('com.miui.calculator:id/btn_2_s').click()

    def three(self):
        self.by_id('com.miui.calculator:id/btn_3_s').click()

    def four(self):
        self.by_id('com.miui.calculator:id/btn_4_s').click()

    def five(self):
        self.by_id('com.miui.calculator:id/btn_5_s').click()

    def six(self):
        self.by_id('com.miui.calculator:id/btn_6_s').click()

    def seven(self):
        self.by_id('com.miui.calculator:id/btn_7_s').click()

    def eight(self):
        self.by_id('com.miui.calculator:id/btn_8_s').click()

    def nine(self):
        self.by_id('com.miui.calculator:id/btn_9_s').click()

    def clear(self):
        self.by_id('com.miui.calculator:id/btn_c_s').click()

    def add(self):
        self.by_id('com.miui.calculator:id/btn_plus_s').click()

    def minus(self):
        self.by_id('com.miui.calculator:id/btn_minus_s').click()

    def equ(self):
        self.by_id('com.miui.calculator:id/btn_equal_s').click()

    def agree(self):
        self.by_id('android:id/button1').click()