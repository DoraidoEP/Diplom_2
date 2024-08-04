import allure
import requests
from data import Data, DataUrl
from helpers import generate_email_user, generate_user_pass, generate_user_name


class TestLoginUser:
    @allure.title('Проверка успешной авторизации')
    @allure.description('Создание и вход в систему на аккаунт пользователя')
    def test_user_login_passed(self):
        # Данные пользователя
        user_data = {
            'email': Data.email,
            'password': Data.password,
            'name': Data.name
        }
        # Отправляем GET-запрос на указанный URL с данными пользователя
        requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        response = requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка авторизации пользователя с неверным паролем')
    @allure.description('Проверка авторизации курьера с неверным паролем  и получения ошибки 401')
    def test_no_such_password(self):
        # Генерируем email, имя пользователя и вводим неверный пароль
        user_data = {
            'email': generate_email_user(),
            'password': Data.incorrect_password,
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными пользователя
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Проверяем, что статус ответа равен 401
        assert response.status_code == 401

    @allure.title('Проверка авторизации пользователя с неверным логином')
    @allure.description('Проверка авторизации пользователя с неверным логином и получения ошибки 401')
    def test_no_such_login(self):
        # Генерируем пароль, имя пользователя и вводим неверный email
        user_data = {
            'email': Data.incorrect_login,
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными пользователя
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Проверяем, что статус ответа равен 401
        assert response.status_code == 401
