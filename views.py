import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

footer = """
    <footer>
        <hr>
        <div>
            <p>&copy;Домашняя работа № 2</p>
        </div>
    </footer>
"""


def index(request):
    html = """
    <body>
        <h1>Добро пожаловать!</h1>
            <p>Магазин</p>
        <hr>
        <div>
            <h2>Меню</h2>
            <p><a href=''>Главная</a></p>
            <p><a href='about'>О вас</a></p>
        </div>
    </body>
    """ + footer
    logger.info(f'Посещение страницы {__name__}: index')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>О вас</h1>
    <p>Всё о вас</p>
    <hr>
    <div>
        <h2>Меню</h2>
        <p><a href='../'>Главная</a></p>
        <p><a href=''>О вас</a></p>
    </div>
    """ + footer
    logger.info(f'Посещение страницы {__name__}: about')
    return HttpResponse(html)
