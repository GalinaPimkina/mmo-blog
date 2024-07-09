# Блог mmo rpg (доска объявлений)

Техническое задание:

1) Пользователи должны иметь возможность зарегистрироваться по e-mail, получив письмо с кодом подтверждения регистрации.
2) После регистрации пользователям становится доступно создание и редактирование объявлений.
3) Объявления состоят из заголовка и текста, внитри которого могут быть картинки, встроенные видео и другой контент.
4) Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста.
5) При отправке отклика на объявление, пользователь-автор объявления должен получить e-mail оповещение.
6) Пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он можен фильтровать отклики по объявлениям, удалять или принимать их.
7) При принятии отклика пользователю, оставившему отклик, должно прийти уведомление.
8) Пользователь должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гильдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
9) Должна быть новостная рассылка.

---------------------------------------------------------------------------------------------------------------------

# Важно!
после создания суперпользователя и применения миграций, необходимо в админ панели сайта создать 3 группы пользователей:
1) admin - администратор, с id=1
2) moderator - модератор, c id=2
3) defaul_user - простой пользователь, c id=3.
Это необходимо сделать перед регистрацией новых пользователей через форму на сайте, т.к. при регистрации всем пользователям автоматически будет назначаться группа defaul_user по умолчанию. Если их не создать заранее, будет ошибка.
---------------------------------------------------------------------------------------------------------------------


На главной странице сайта (доске объявлений) всем неавторизованным пользователям доступна следующая навигация по сайту:
![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/2ec3663f-bedf-422a-bdbd-f4af58f046ac)

После регистрации и авторизации на сайте ему открывается дополнительный функционал:
![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/4edc4150-4838-4c67-a273-feae4e3770a8)

Создать новое объявление можно по ссылке "Создать заявку". Поле "Контент" реализовано с помощью ckeditor.
При создании заявки необходимо указывать категорию(класс персонажа). Через админ панель можно добавить все необходимые классы.

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/14a68e66-cae5-40eb-9487-69cae86b1a51)






