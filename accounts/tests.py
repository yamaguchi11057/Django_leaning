from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
# Create your tests here.

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super.setUpClass()
        return super().setUpClass()
        cls.selenium = WebDriver(executable_path='/Users/tsuyoshi/Documents/Python_project/Django_leaning/venv/bin')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super.tearDownClass()
    
    def test_Login(self):
        #ログインページを開く
        self.selenium.get('http://localhost:8000'+str(reverse_lazy('account_login')))

        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('test_mail@test.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("testpass")
        self.selenium.find_element_by_class_name('btn').click()

        #ページタイトル検証
        self.assertEquals('日記一覧 | PrivateDiary', self.selenium.title)