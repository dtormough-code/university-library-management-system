# University Library Management System

A web-based library management system developed to help a university manage its book collection and make book information easier to access.

## Features

- View books in the library catalogue.
- Display book titles, authors, ISBNs, and categories.
- Track total books and available copies.
- Manage book records through the Django administration panel.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Project Structure

```text
library_management/
├── config/                 # Django project configuration
├── library/                # Library application
│   ├── migrations/         # Database migrations
│   ├── templates/
│   │   └── library/
│   │       └── home.html   # Library dashboard
│   ├── admin.py            # Admin configuration
│   ├── models.py           # Book data model
│   ├── urls.py             # Application routes
│   └── views.py            # Application logic
├── .gitignore
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/dtormough-code/university-library-management-system.git
cd university-library-management
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Administration

To create an administrator account, run:

```bash
python manage.py createsuperuser
```

Then access the Django administration panel at `http://127.0.0.1:8000/admin/`.

## Current Status

The project includes a book data model, Django administration, and a library dashboard for displaying book information and collection statistics. Further improvements can include book search, borrowing and returning workflows, student records, and overdue-book tracking.

## Author

**dtormough-code**

GitHub: https://github.com/dtormough-code
