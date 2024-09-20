from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        page_elements = {
    'calculator_screen': Element('//input[@id="calculator-screen"]', self),
    '1': Element('//button[@id="key-1"]', self),
    '2': Element('//button[@id="key-2"]', self),
    '3': Element('//button[@id="key-3"]', self),
    'key_add': Element('//button[@id="key-add"]', self),
    '4': Element('//button[@id="key-4"]', self),
    '5': Element('//button[@id="key-5"]', self),
    '6': Element('//button[@id="key-6"]', self),
    'key_subtract': Element('//button[@id="key-subtract"]', self),
    '7': Element('//button[@id="key-7"]', self),
    '8': Element('//button[@id="key-8"]', self),
    '9': Element('//button[@id="key-9"]', self),
    'key_multiply': Element('//button[@id="key-multiply"]', self),
    '0': Element('//button[@id="key-0"]', self),
    'key_decimal': Element('//button[@id="key-decimal"]', self),
    'key_clear': Element('//button[@id="key-clear"]', self),
    'key_divide': Element('//button[@id="key-divide"]', self),
    'key_equals': Element('//button[@id="key-equals"]', self),
    'remote_toggle' : Element('//button[@id="remote-toggle"]', self),
    'open_history' : Element('//button[@id="toggle-button"]', self),
    'logout': Element('//button[@id="logout-button"]', self),
    'username': Element('//label[@id="user-name"]', self),
    'text_window': Element('//div[@id="text-window"]', self),
    'clear_history': Element('//button[@id="clear-history"]', self),
    'history': Element('//textarea[@id="history"]', self),
}


        self.elements = munchify(page_elements)

    def add(self, number1, number2):
        self.elements.__getitem__(str(number1)).click()
        self.elements.key_add.click()
        self.elements.__getitem__(str(number2)).click()
        self.elements.key_equals.click()
        return int(self.elements.calculator_screen.value)
    
    def sub(self, number1, number2):
        self.elements.__getitem__(str(number1)).click()
        self.elements.key_subtract.click()
        self.elements.__getitem__(str(number2)).click()
        self.elements.key_equals.click()
        return int(self.elements.calculator_screen.value)
    
    def mul(self, number1, number2):
        self.elements.__getitem__(str(number1)).click()
        self.elements.key_multiply.click()
        self.elements.__getitem__(str(number2)).click()
        self.elements.key_equals.click()
        return int(self.elements.calculator_screen.value)
    
    def divide(self, number1, number2):
        self.elements.__getitem__(str(number1)).click()
        self.elements.key_divide.click()
        self.elements.__getitem__(str(number2)).click()
        self.elements.key_equals.click()
        return int(self.elements.calculator_screen.value)
    
    def history_text(self):
        self.elements.open_history.click()
        return self.elements.history.value