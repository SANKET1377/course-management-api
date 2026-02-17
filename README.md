# 📚 Course Management API

A scalable RESTful backend API built with **FastAPI** and **MongoDB**, supporting course management, chapter-based ratings, automated testing with PyTest, and Docker-based containerization.

---

## 🚀 Features

* Retrieve all courses with sorting options:

  * Alphabetical order
  * Date (latest first)
  * Aggregated rating
* Filter courses by domain
* Get detailed course overview
* Retrieve specific chapter details
* Rate individual chapters (positive / negative)
* Automatically aggregate course ratings
* Automated API testing with PyTest
* Containerized deployment using Docker

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MongoDB
* **Testing:** PyTest
* **Containerization:** Docker
* **Server:** Uvicorn

---

## 📂 Project Structure

```
.
├── main.py            # FastAPI application and API endpoints
├── script.py          # Data loading script (JSON → MongoDB)
├── test_app.py        # Automated API tests
├── courses.json       # Sample course data
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create the folder


---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate (Windows):

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Start MongoDB

Ensure MongoDB service is running locally at:

```
mongodb://localhost:27017/
```

---

### 5️⃣ Load Sample Data

```
python script.py
```

---

### 6️⃣ Run the API

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

```
pytest
```

This validates:

* Sorting logic
* Filtering logic
* Course retrieval
* Chapter retrieval
* Rating functionality
* Error handling

---

## 🐳 Docker Deployment

### Build Image

```
docker build -t course-api .
```

### Run Container

```
docker run -d -p 80:80 course-api
```

Access API at:

```
http://localhost/docs
```

---

## 📊 API Endpoints

| Method | Endpoint                            | Description                                   |
| ------ | ----------------------------------- | --------------------------------------------- |
| GET    | `/courses`                          | Retrieve all courses with sorting & filtering |
| GET    | `/courses/{course_id}`              | Get course overview                           |
| GET    | `/courses/{course_id}/{chapter_id}` | Get chapter details                           |
| POST   | `/courses/{course_id}/{chapter_id}` | Rate a chapter                                |

---

## 🧠 Architecture Overview

```
Client → FastAPI → MongoDB
                ↘ PyTest (Testing)
                ↘ Docker (Deployment)
```

---

## 🎯 Learning Outcomes

* Designed RESTful APIs using FastAPI
* Integrated MongoDB with PyMongo
* Implemented rating aggregation logic
* Built automated test cases using PyTest
* Containerized backend application with Docker
* Managed environment configuration and dependency isolation

---

## 👨‍💻 Author

**Sanket Darekar**
FastAPI | Python | MongoDB
