# Full Stack Contact Manager App (React + Flask)

A simple full-stack CRUD web application built with **React.js** on the frontend and **Flask** (with SQLAlchemy) on the backend. This app allows users to create, read, update, and delete contact records consisting of a **first name**, **last name**, and **email address**.

---

## 🛠 Tech Stack

### Frontend
- [React.js](https://reactjs.org/)
- Fetch API or Axios for HTTP requests
- CSS for styling

### Backend
- [Flask](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/) for handling cross-origin requests
- [SQLAlchemy](https://www.sqlalchemy.org/) ORM
- SQLite

---

## 🚀 Features

- 📄 **View all contacts**  
- ➕ **Add a new contact**  
- ✏️ **Edit existing contact details**  
- ❌ **Delete a contact**  
- 🔁 **Frontend syncs dynamically with backend state**

---

## 📁 Project Structure
/project-root
│
├── backend/
│ ├── app.py # Flask app and API routes
│ ├── models.py # SQLAlchemy models
│ ├── config.py # DB and Flask app setup
│ └── ...
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── ContactForm.jsx
│ │ ├── ContactList.jsx
│ │ └── index.css
│ └── ...
│
├── README.md

