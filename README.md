"# django-project"  
# Онлайн-платформа заказа дизайна

## 🚀 Основной функционал
* **Интерактивные формы:** простой сайт для вывода новостей и проектов для работы с админкой + отправка писем на почту

## 🛠 Стек технологий
* **Backend:** Python 3.x, Django, Django Forms
* **Frontend:** HTML5, CSS3, SCSS, JavaScript
* **База данных:** SQLite (для локального теста)

## 💻 Как запустить проект локально

1. Клонируйте репозиторий:
git clone https://github.com/ShitCodeEver/project.git

2. Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows

3. Установите зависимости:
pip install -r requirements.txt

4. Выполните миграции:
python manage.py migrate

5. Запустите локальный сервер:
python manage.py runserver
