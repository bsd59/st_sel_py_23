# from .base_page import BasePage
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверку на корректный url (-содержит подстроку "login")
        current_url = self.browser.current_url
        assert "login" in current_url, 'Substring "login" is not in the current browser url'

    def should_be_login_form(self):
        # проверка -форма логина содержит все элементы
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit is not presented"

    def should_be_register_form(self):
        # проверку -форма регистрации содержит все элементы
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit is not presented"
