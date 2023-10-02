from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        # adicione quaisquer funções globais aqui, por exemplo:
        # 'static': staticfiles_storage.url,
    })
    return env