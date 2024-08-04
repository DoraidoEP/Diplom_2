import allure
import requests
from data import DataUrl
from helpers import generate_email_user, generate_user_pass, generate_user_name


class TestChangeUser:
    @allure.title('Проверка изменения данных пользователя')
    @allure.description('Проверка создания пользователя и изменения его данных')
    def test_changing_user_data_from_authorization(self):
        # Генерируем данные для регистрации первого пользователя
        user_data_1 = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Генерируем данные для регистрации второго пользователя
        user_data_2 = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # f'{url_constants.URL + url_constants.LOGIN_USER}'
        # Отправляем POST-запрос на указанный URL(создание пользователя) с данными первого пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data_1)
        # Отправляем POST-запрос на указанный URL(вход в систему) с данными первого пользователя
        user_data = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data_1)
        # Извлечение токена доступа
        token = user_data.json()['accessToken']
        # Отправляем GET-запрос на указанный URL на изменение данных пользователя
        response = requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_changing_user_data}',
                                headers={'Authorization': token}, data=user_data_2)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @allure.description('Проверка создания пользователя и изменения его данных без авторизации')
    def test_changing_user_data_without_authorization(self):
        # Генерируем данные для регистрации первого пользователя
        user_data_1 = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Генерируем данные для регистрации второго пользователя
        user_data_2 = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL(создание пользователя) с данными первого пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data_1)
        # Отправляем GET-запрос на указанный URL на изменение данных пользователя
        response = requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_changing_user_data}', data=user_data_2)
        # Проверяем, что статус ответа равен 401
        assert response.status_code == 401
