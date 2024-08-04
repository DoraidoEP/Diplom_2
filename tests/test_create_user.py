import allure
import requests
from data import Data, DataUrl
from helpers import generate_email_user, generate_user_pass, generate_user_name


class TestCreateUser:
    @allure.title('Проверка создания нового пользователя')
    @allure.description('Создание и проверка нового пользователя')
    def test_create_user(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email, пароле и имени пользователя
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка того, что нельзя создать двух пользователей с одинаковым логином')
    @allure.description('Отправка двух запросов на создание пользователя с одинаковыми данными')
    def test_create_user_double_login_not_created(self):
        # Генерируем пароль и имя пользователя для регистрации. Используем существующий email
        user_data = {
            'email': Data.email,
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email, пароле и имени пользователя
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data)
        # Проверяем, что статус ответа равен 403
        assert response.status_code == 403

    @allure.title('Проверка создания нового пользователя без обязательного поля')
    @allure.description('Отправка запроса на создание пользователя без заполненного поля "password"')
    def test_create_user_missing_field_error(self):
        # Генерируем только email и имя пользователя для регистрации
        user_data = {
            'email': generate_email_user(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email и имени пользователя
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data)
        # Проверяем, что статус ответа равен 403
        assert response.status_code == 403
