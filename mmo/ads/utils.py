mainmenu = [
    {'title': 'Главная страница', 'url_name': 'ads:index'},
    {'title': 'Все объявления', 'url_name': 'ads:all_posts'},
    {'title': 'Объявления по классам', 'url_name': 'ads:categories'},
    ]

auth_menu = [
    {'title': 'Создать заявку', 'url_name': 'ads:add_post'},
    {'title': 'Мои объявления', 'url_name': 'ads:user_post_page'},
    {'title': 'Входящие отклики', 'url_name': 'ads:comments_incoming'},
    {'title': 'Мои отклики', 'url_name': 'ads:comments_outgoing'},
]

logout_menu = [
    {'title': 'Выйти', 'url_name': 'users:logout'},
]

login_signup_menu = [
    {'title': 'Войти', 'url_name': 'users:login'},
    {'title': 'Регистрация', 'url_name': 'users:registration'},
]

class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['mainmenu'] = mainmenu
        context['auth_menu'] = auth_menu
        context['logout_menu'] = logout_menu
        context['login_signup_menu'] = login_signup_menu
        context.update(kwargs)
        return context
