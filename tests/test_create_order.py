import allure
import requests
from data import DataUrl, Ingredients
from helpers import generate_email_user, generate_user_pass, generate_user_name


class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизованным пользователем')
    @allure.description('Проверка создания заказа с существующими ингредиентами авторизованным пользователем')
    def test_create_order_ingredients_authorized_user(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
                'email': generate_email_user(),
                'password': generate_user_pass(),
                'name': generate_user_name()
        }
        # Отправляем POST и GET запросы на указанный URL с данными о email, пароле и имени пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        requests.get(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Отправляем POST-запрос на указанный URL с данными об ингредиентах
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_order}', data=Ingredients.burger_existing)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка создания заказа неавторизованным пользователем')
    @allure.description('Проверка создания заказа с существующими ингредиентами неавторизованным пользователем')
    def test_create_order_ingredients_unauthorized_user(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
                'email': generate_email_user(),
                'password': generate_user_pass(),
                'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email, пароле и имени пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Отправляем POST-запрос на указанный URL с данными об ингредиентах
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_order}',
                                 data=Ingredients.burger_existing)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 200

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Проверка создания заказа без ингредиентов авторизованным пользователем')
    def test_create_order_authorized_user_no_ingredients(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
                'email': generate_email_user(),
                'password': generate_user_pass(),
                'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email, пароле и имени пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Отправляем POST-запрос на указанный URL с данными об ингредиентах
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_order}', data=Ingredients.burger_empty)
        # Проверяем, что статус ответа равен 200
        assert response.status_code == 400

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description('Проверка создания заказа с неверным хешем ингредиентов авторизованным пользователем')
    def test_create_order_authorized_user_bad_ingredients_hash_error(self):
        # Генерируем данные для регистрации пользователя
        user_data = {
                'email': generate_email_user(),
                'password': generate_user_pass(),
                'name': generate_user_name()
        }
        # Отправляем POST-запрос на указанный URL с данными о email, пароле и имени пользователя
        requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_login_user}', data=user_data)
        # Отправляем POST-запрос на указанный URL с данными об ингредиентах
        response = requests.post(f'{DataUrl.Url_main_page + DataUrl.Url_order}', data=Ingredients.non_existent_burger)
        # Проверяем, что статус ответа равен 500
        assert response.status_code == 500
