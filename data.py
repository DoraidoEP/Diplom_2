class Data:

    name = 'Eduard'
    email = 'DoraidoPavlov@yandex.ru'
    password = 'DoraidoEP123'
    incorrect_password = 'Dobrinya12'
    incorrect_login = 'vasyapushkin@mail.ru'


class DataUrl:
    Url_main_page = 'https://stellarburgers.nomoreparties.site'

    Url_create_user = '/api/auth/register'
    Url_login_user = '/api/auth/login'
    Url_changing_user_data = '/api/auth/user'

    Url_order = '/api/orders'


class Ingredients:
    burger_existing = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    non_existent_burger = {'ingredients': ['"43d3463f7034a000269f45e7', '56d3463f7034a000269f45e9']}
    burger_empty = {'ingredients': ''}