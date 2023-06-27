## Тестовое задание на позицию Junior Python Developer

В этом тестовом задании Вам нужно разработать онлайн каталог сотрудников для
компании с более чем 50,000 сотрудников.
Общая информация
1. Тестовое задание разделено на две части. Часть N1 обязательная и мы
примем Вашу кандидатуру к рассмотрению только в том случае если часть N1
выполнена. Часть N2 опциональная, по количеству задач из этой части
которые Вы смогли выполнить мы сможем оценить Ваш уровень опыта и
навыков в области веб разработки. Если у Вас уже есть опыт работы с
фреймворками Django и/или Flask – попытайтесь выполнить все или как можно
больше задач из части N2, это повысит ваши шансы по отношению к другим
кандидатам.
2. Вы должны отправить Ваше решение для тестового задания на нашу
электронную почту hr@abz.agency в виде ссылки на github/bitbucket
репозиторий. Если Вы пришлете Ваше решение в любом другом виде (в виде
ссылки на zip архив, прикрепите zip архив к письму, и др.) – Ваша кандидатура
не будет нами рассмотрена!
3. Вам необходимо также приложить ссылку или вложением подробное резюме,
контактный номер телефона и ник скайпа.
4. Укажите в письме список выполненных пунктов для каждой части, выбранный
вами фреймворк. Если Вы сделали не все пункты тестового задания –
пожалуйста, укажите причину по которой вы их не выполнили (не хватило
времени, не хватает опыта/знания, что-то ещё).

Технические требования
- Django 2.1+ / Flask 1.0+
- MySQL 5.6+ / PostgreSQL 10+
- Python 3.7+

При выполнении тестового задания Вы можете дополнительно использовать любые
сторонние Python и/или Javascript/CSS библиотеки, без всяких ограничений. Все 3rd
party Python/Javascript/CSS библиотеки должны быть добавлены в проект через
pip/bower/npm/yarn если библиотека поддерживает такой способ установки. У нас
нет никаких требований к оформлению фронтенд части, но аккуратный вид
приветствуется и добавим вам бонусных пунктов.

### Часть N1 (обязательная)
Создайте веб страницу, которая будет выводить иерархию сотрудников в
древовидной форме.

Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные:
- ФИО;
- Должность;
- Дата приема на работу;
- Размер заработной платы;

1. У каждого сотрудника есть 1 начальник;
2. База данных должна содержать не менее 50 000 сотрудников и 5 уровней
иерархий.
3. Не забудьте отобразить должность сотрудника.

### Часть N2 (опциональная)
1. Создайте базу данных используя миграции Django / Flask.
2. Используйте DB seeder для Django ORM / Flask-SQLAlchemy для заполнения
базы данных.
3. Используйте Twitter Bootstrap для создания базовых стилей Вашей страницы.
4. Создайте еще одну страницу и выведите на ней список сотрудников со всей
имеющейся о сотруднике информацией из базы данных и возможностью
сортировать по любому полю.
5. Добавьте возможность поиска сотрудников по любому полю для страницы
созданной в задаче 4.
6. Добавьте возможность сортировать (и искать если Вы выполнили задачу No5)
по любому полю без перезагрузки страницы, например используя ajax.
7. Используя стандартные функции Django / Flask, осуществите аутентификацию
пользователя для раздела веб сайта доступного только для
зарегистрированных пользователей.
8. Перенесите функционал разработанный в задачах 4, 5 и 6 (используя ajax
запросы) в раздел доступный только для зарегистрированных пользователей.
9. В разделе доступном только для зарегистрированных пользователей,
реализуйте остальные CRUD операции для записей сотрудников. Пожалуйста
заметьте, что все поля касающиеся пользователей должны быть
редактируемыми, включая начальника каждого сотрудника.
10. Осуществите возможность загружать фотографию сотрудника и отобразите ее
на странице, где можно редактировать данные о сотрудник. Добавьте
дополнительную колонку с уменьшенной фотографией сотрудника на
странице списка всех сотрудников.
11. Осуществите возможность перераспределения сотрудников в случае
изменения начальника (бонусом может быть то, что вы сможете это
осуществить с применением встроенных механизмов/парадигм, предлагаемых
Django ORM / Flask-SQLAlchemy ORM).
12. Реализуйте ленивую загрузку для дерева сотрудников. Например, показывайте
первые два уровня иерархии по умолчанию и подгружайте 2 следующих
уровня или всю ветку дерева при клике на сотрудника второго уровня.
13. Реализуйте возможность менять начальника сотрудника используя drag-n-drop
сразу в дереве сотрудников.