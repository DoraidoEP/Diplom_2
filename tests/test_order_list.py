import allure
import requests
from data import DataUrl
from helpers import generate_email_user, generate_user_pass, generate_user_name


class TestOrderList:
    @allure.title('Проверка получения списка заказов c авторизованным пользователем')
    @allure.description('Проверка получения списка заказов авторизованным пользователем и получения статус 200')
    def test_get_list_order(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL(создание пользователя) с данными пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data)
        # Отправляем POST-запрос на указанный URL(вход в систему) с данными пользователя
        login = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Извлечение токена доступа
        token = login.json()['accessToken']
        # Отправляем GET-запрос на указанный URL для получения списка заказов
        response = requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_order}',
                                headers={'Authorization': token}, data=user_data)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка получения списка заказов c неавторизованным пользователем')
    @allure.description('Проверка получения списка заказов c неавторизованным пользователем и получения статус 401')
    def test_get_list_order(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
            'email': generate_email_user(),
            'password': generate_user_pass(),
            'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL(создание пользователя) с данными пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_create_user}', data=user_data)
        # Отправляем GET-запрос на указанный URL для получения списка заказов
        response = requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_order}', data=user_data)
        # Проверяем, что статус ответа равен 401
        assert response.status_code == 401
