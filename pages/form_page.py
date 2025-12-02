from pages.base_page import BasePage

class FormPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://example.com/form"

        self.name_input = "#name"
        self.email_input = "#email"
        self.phone_input = "#phone"
        self.address_input = "#address"
        self.submit_btn = "#submit"
        self.success_msg = ".success-msg"

    def open(self):
        self.page.goto(self.url)

    def fill_form(self, name, email, phone, address):
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.fill(self.phone_input, phone)
        self.fill(self.address_input, address)
        self.click(self.submit_btn)

    def get_success_message(self):
        return self.get_text(self.success_msg)
