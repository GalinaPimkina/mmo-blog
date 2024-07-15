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

Используется база данный PostgreSQL, параметры прописаны в settings.py

После создания суперпользователя и применения миграций, необходимо в админ панели сайта создать 3 группы пользователей:
1) admin - администратор, с id=1
2) moderator - модератор, c id=2
3) default_user - простой пользователь, c id=3.   
Это необходимо сделать перед регистрацией новых пользователей через форму на сайте, т.к. при регистрации всем пользователям автоматически будет назначаться группа default_user по умолчанию. Если их не создать заранее, ошибка будет отработана исключением, а вы попадете на страницу с инструкцией.
---------------------------------------------------------------------------------------------------------------------


На главной странице сайта (доске объявлений) всем неавторизованным пользователям доступна следующая навигация по сайту:
![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/2ec3663f-bedf-422a-bdbd-f4af58f046ac)

После регистрации и авторизации на сайте ему открывается дополнительный функционал:
![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/4edc4150-4838-4c67-a273-feae4e3770a8)

Создать новое объявление можно по ссылке "Создать заявку". Поле "Контент" реализовано с помощью ckeditor.
При создании заявки необходимо указывать категорию(класс персонажа). Через админ панель можно добавить все необходимые классы.

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/14a68e66-cae5-40eb-9487-69cae86b1a51)

На главной странице со всеми объявлениями о поиске все заголовки кликабельны, можно перейти к конкретному объявлению

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/c3f81b4f-d911-4f13-ac3a-c129c9a19b4b)

Находясь внутри объявления, можно ответить на него, Кликнув по ссылке "Откликнуться" справа 

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/28ae5fd1-dfb8-4f84-85fa-58b80da40b75)

После отправки отклика 

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/02e48f6b-c726-496f-b1f4-a6faf99804ca)

Можно просмотреть список всех своих отправленных откликов по ссылке "Мои отклики". Справа на каждом отклике можно посмотреть его статус - Ожидает рассмотрения, Принят или Отклонен

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/5ac4edbe-5d92-40c3-bd83-3c1e646dd763)

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/818713c4-03e0-4fdc-a4ef-7bf434dfa192)

После отправки отклика, автор объявления получит на почту оповещение о нем

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/1afd0640-2258-4c42-8095-91932385dbca)

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/f2249847-a74a-4bde-a29a-3cc9e27a27e4)

Перейдя по ссылке, автор объявления увидит страницу с этим откликом

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/b68e3306-3e81-4611-8747-a810c186eaff)

Он может принять его или отклонить(я так реализовала функционал удаления, rejected=True ). В зависимости от его действий, на сайте будет выведена информация о статусе отклика как для автора объявления, так и для автора отклика.

Автор отклика получит оповещение после действий с его откликом.

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/d4c149ec-a1c0-4cd3-bf41-9b7305777f9d)

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/b859502b-bdf5-4e81-a0e1-ec389833667f)

Если автор объявления нашел себе нужного человека, и объявление больше не актуально, автор объявления может его закрыть. После чего никто из пользователей не сможет на него откликаться. 

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/07899bd6-58ff-451d-9f4c-905773a60129)

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/20fc3942-78c2-4d79-b98b-781709d29f47)

Перейдя по ссылке "Объявления по классам" в главном меню, можно увидеть список категорий(классов). Кликнув по нужной, попадаешь в объявления, отфильтрованные по текущей категории(классу). 

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/82cfcb00-e921-407a-a478-7150a3cd55ed)

На этой странице можно увидеть ссылку подписки на текущую категорию, что позволит получать оповещения на почту, если кто-то из пользователей создаст объявление в текущей категории(классе).

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/a243353b-50e2-4a6b-9ba8-582cc28207e0)

Без подписки на категорию(класс) профиль пользователя выглядел так:

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/9f00c05a-6d22-4598-a706-1fbebfb6896e)

После подписки

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/5ec94945-d47c-4bc8-95a1-b883016420f9)

Профиль выглядит так:

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/b3a7d80a-d6f5-4cbb-b326-e9eff7241654)

Можно отписаться от текущей подписки, тогда оповещения об обновлениях перестанут приходить.

Так же на панели меню есть вкладка "Новости". Там выкладываются все новости платформы. Их создает админ состав из панели администратора. Рассылка уведомлений на почту идет всем пользователям.

![изображение](https://github.com/GalinaPimkina/mmo-blog/assets/133103137/78a22e2f-f353-49e9-a1fa-7d7781a4c5ac)





















