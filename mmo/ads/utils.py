class DataMixin:
    '''для расширения контекста'''
    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context


def get_filename(filename, request):
    return filename.upper()