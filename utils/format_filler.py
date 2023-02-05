from page_objects.base_page import BasePage


class ContactUsForm(BasePage):
    def __init__(self, driver, name, email, subject, message):
        self.name = name
        self.email = email
        self.message = message
        self.subject = subject
        super(ContactUsForm, self).__init__(driver)

    def fill_form(self, **elements):
        self.fill_text(elements['name'], self.name)
        self.fill_text(elements['email'], self.email)
        self.fill_text(elements['subject'], self.subject)
        self.fill_text(elements['message'], self.message)
