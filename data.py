class Data:

    name = 'Eduard'
    email = 'DoraidoPavlov@yandex.ru'
    password = 'DoraidoEP123'
    incorrect_password = 'Dobrinya12'
    incorrect_login = 'vasyapushkin@mail.ru'


class DataUrl:
    Url_main_page = 'https://stellarburgers.nomoreparties.site/'
    Url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    Url_login_user = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    Url_changing_user_data = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    Url_create_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    Url_orders_from_user = 'https://stellarburgers.nomoreparties.site/api/orders'


class Ingredients:
    burger_existing = {'ingredients': ['60d3b41abdacab0026a733c6', '609646e4dc916e00276b2870']}
    non_existent_burger = {'ingredients': ['"43d3463f7034a000269f45e7', '56d3463f7034a000269f45e9']}
    burger_empty = {'ingredients': ''}
