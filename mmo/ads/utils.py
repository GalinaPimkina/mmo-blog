menu = [
    {'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'Добавить новость', 'url_name': 'add_news'},
    {'title': 'Поиск пати', 'url_name': 'all_posts'},
    {'title': 'Создать заявку', 'url_name': 'add_post'},
    {'title': 'Войти', 'url_name': 'users:login'},
]


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context
