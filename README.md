# 🛒 Django Cart & Shop API

Цей проєкт — це приклад e-commerce вебзастосунку, створеного на **Django** з використанням **Django REST Framework (DRF)**.  
Він дозволяє працювати з каталогом товарів, кошиком покупця, а також надає REST API для інтеграції з фронтендом або мобільним застосунком.

---

## 🚀 Основні можливості

### 🏬 Каталог товарів
- Перегляд списку всіх товарів з пагінацією
- Фільтрація за категорією (`?category=fruits`)
- Перегляд детальної інформації про товар
- Зображення товарів з однаковими пропорціями

### 🛍️ Кошик
- Додавання товарів у кошик
- Збільшення/зменшення кількості (+ / -)
- Видалення окремих позицій
- Очищення всього кошика
- Підрахунок загальної суми

### 🔗 REST API (DRF)
| Метод | Ендпоінт | Опис |
|:------|:----------|:-----|
| `GET` | `/api/products/` | Отримати список товарів (з фільтрацією та пагінацією) |
| `GET` | `/api/products/{id}/` | Отримати деталі товару |
| `GET` | `/api/cart/` | Переглянути поточний стан кошика |
| `POST` | `/api/cart/` | Додати або оновити товар у кошику |
| `DELETE` | `/api/cart/{product_id}/` | Видалити товар із кошика |

---

## ⚙️ Технології

- **Python 3.10+**
- **Django 4.2+**
- **Django REST Framework**
- **PostgeSQL**
- **HTML / CSS (Jinja templates)**

---

## 📦 Встановлення

1. **Клонування репозиторію**
   ```bash
   git clone https://github.com/Randayy/django-cart-task.git
   cd django-cart-api

2. **Створення віртуального середовища**
   ```bash
   python -m venv venv
   source venv/bin/activate  # для macOS / Linux
   venv\Scripts\activate     # для Windows
   
3. **Встановлення залежностей**
   ```bash
   pip install -r requirements.txt

4. **Міграції бази даних**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
5. **Cтворення суперюзера для адмінки**
   ```bash
   python manage.py createsuperuser

6. **Запуск сервера**
   ```bash
   python manage.py runserver

## Перевірка роботи

🌐 Головна сторінка: http://127.0.0.1:8000/

🧾 Список товарів: http://127.0.0.1:8000/shop/products

🛒 Кошик: http://127.0.0.1:8000/shop/cart/

⚙️ API: http://127.0.0.1:8000/api/
 


