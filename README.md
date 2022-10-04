# **YuraOffersPlaces**
[![Python](https://img.shields.io/badge/Python-3.10.6-lightgreen?logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.1.1-lightgreen?logo=Django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.2.1-lightgreen?logo=Bootstrap)](https://getbootstrap.com/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)

## **Описание/Description:**
Курсовая работа для моего племянника в универе. Сервис, предлагающий пользователю 3 релеватных места (по данным 2GIS), исходя из выбранной категории. IP определяется автоматически. Местоположение определяется по данным Dadata. В сервисе также реализованы регистрация и авторизация, возможность редактирования профиля и просмотр 5 предыдущих запросов.

---

### В данном проекте реализованы:
- Авторизация Django (+ смена пароля);
- Работа со сторонними API (2GIS и Dadata);
- Автоматическое сохранение последних 5 запросов пользователя;
- Шаблонизация (в том числе с использованием иерархии шаблонов и фреймворка Bootstrap);
- Контейнеризация Docker и Docker Compose с разворачиванием проекта при помощи Nginx, Gunicorn;
- Получение в целях безопасности переменных окружения из файла .env.

---

### **Автор/Author:**
[Nikita Natalenko](https://github.com/kitahkitah/)
