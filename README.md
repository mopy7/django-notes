# Django Notes 📝

A minimal, modern, authenticated notes application built with Django.

This project focuses on **clean architecture**, **proper authentication**, and **ownership-based access control**, without unnecessary complexity.

---

## ✨ Features

- User authentication (login / logout)
- Create, read, update, and delete notes (CRUD)
- Notes are **private** and scoped to the logged-in user
- Clean, minimal UI (no frontend frameworks)
- Class-Based Views (CBVs)
- Slug-based note URLs
- Secure access using `LoginRequiredMixin`

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates + CSS
- **Database:** SQLite (default, can be swapped)
- **Auth:** Django built-in authentication system

---

## 📂 Project Structure (simplified)
```bash
src/
├── core/
│ └── urls.py
├── notes/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── notes/
├── templates/
│ └── registration/
│ └── login.html
├── static/
│ └── css/
│ └── app.css
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/django-notes.git
cd django-notes

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate

python manage.py migrate

python manage.py runserver
```

---

## Authentication Notes:

  - Uses Django’s built-in authentication system
  - All pages require user login
  - Login and logout are handled via Django auth views
  - User signup is intentionally not implemented
  - Users are created through the Django admin panel
  - Notes are private and accessible only to their owner
  - Access control is enforced using LoginRequiredMixin
  - Querysets are filtered by the logged-in user to ensure data isolation

## Design Philosophy:
  - Minimal and distraction-free user interface
  - Focus on readability and usability
  - No frontend frameworks used
  - Relies on spacing, typography, and layout instead of heavy styling
  - Designed to feel like a real internal tool
  - Prioritizes clarity and maintainability
  - Avoids unnecessary JavaScript and visual noise
