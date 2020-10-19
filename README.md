# django-blog

Это мой первый тестовый блог на django, над которым я еще работаю!

![alt tag](https://github.com/pro100git/django-blog/blob/main/Screenshot/Screenshot.png "django blog")​

### Зависимости:
pip install --user -r requirements.txt

### Что реализовано:
* Кастомизирована модель User 
* Регистрация (без подтверждения почты)
* Смена пароля (с отправкой на почту ссылки для смены пароля)
В файле **settings.py** на 139 и 140 строках, нужно указать gmail аккаунт
* Страница пользователя (Биография, Статус, Соц.сети (с валидацией), Ссылки на все посты пользователя)
* Комментарии с модерацией без доступа к админ панели
* Количество просмотров поста, лайки (без ajax), теги, блок поделиться
* Вывод популярных постов (сортировка по кол-ву просмотров)
* Добавление постов, через форму с автоматическим определением автора
* Автоматическая генерация url адреса, используются поля title и id
* Пагинация
* Поиск по сайту
* Каптча
* Редактор CKeditor

