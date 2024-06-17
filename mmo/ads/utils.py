menu = [
    {'title': 'Главная страница', 'url_name': 'ads:index'},
    {'title': 'Добавить новость', 'url_name': 'ads:add_news'},
    {'title': 'Поиск пати', 'url_name': 'ads:all_posts'},
    {'title': 'Создать заявку', 'url_name': 'ads:add_post'},
]


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context
