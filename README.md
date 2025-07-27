# 🧑‍💼 Django Employee Management System

This is a fully functional employee management web application built using **Django** and **Bootstrap**.

---

## 🔧 Tech Stack

- **Backend**: Django (5.x), Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite3 (default), switchable to PostgreSQL/MySQL
- **Authentication**: Django auth (Login/Register/Logout)
- **Media Handling**: Resume + Profile Picture Upload

---

## ✅ Features

- 🔐 **Admin/HR Login & Role-Based Access**
- 🧾 **Employee CRUD Operations**
- 🖼️ **Profile Picture Upload**
- 📄 **Resume Upload (PDF)**
- 🔎 **Search/Filter Employees**
- 📤 **REST API Integration**
- 📁 **Bootstrap Frontend with Validation**

---

## 🚀 Run Locally

```bash
# Clone project
git clone https://github.com/YOUR_USERNAME/employee-management.git
cd employee-management

# Create virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run server
python manage.py migrate
python manage.py runserver


Author Sourav Salunkhe
