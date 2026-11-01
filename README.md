# AI Resume Analyzer 📄

A Django-based Resume Analyzer that extracts text from PDF resumes and compares candidates' skills with a given job description. It identifies matching skills, missing skills, and calculates a job match percentage.

## 🚀 Project Overview

The AI Resume Analyzer is a Python Django web application designed to simplify the initial resume screening process.

Users can upload their resumes in PDF format and enter a job description. The application extracts text from the uploaded resume, identifies relevant skills, compares them with the job description, and displays a match score.

This project demonstrates Python full-stack development, PDF text extraction, backend processing, and database integration.

## ✨ Features

* **PDF Resume Upload:** Upload resumes in PDF format.
* **Text Extraction:** Extract text from uploaded PDF resumes.
* **Job Description Matching:** Compare resume content with job requirements.
* **Skill Identification:** Identify matching skills.
* **Missing Skills Detection:** Display skills that are missing from the resume.
* **Match Percentage:** Calculate a resume match score based on matched skills.
* **Database Integration:** Store resume analysis results using SQLite.
* **User-Friendly Interface:** Simple and responsive frontend design.
* **Input Validation:** Check uploaded file type and required fields.

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend programming       |
| Django     | Web application framework |
| HTML5      | Frontend structure        |
| CSS3       | Website styling           |
| JavaScript | Frontend interactivity    |
| SQLite     | Database management       |
| PyPDF      | PDF text extraction       |
| Git        | Version control           |
| GitHub     | Project hosting           |

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── resume_app/
│   ├── migrations/
│   ├── static/
│   │   └── resume_app/
│   │       ├── script.js
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── resume_app/
│   │       ├── index.html
│   │       └── result.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/narenderkoyalkardavke-tech/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install django pypdf
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Visit the following address in your browser:

http://127.0.0.1:8000/

## 🔍 How It Works

1. Open the AI Resume Analyzer application.
2. Upload a resume in PDF format.
3. Enter the job description.
4. Click the **Analyze Resume** button.
5. The application extracts text from the uploaded PDF.
6. The system identifies required skills from its predefined skill list.
7. It compares those skills with the extracted resume text.
8. The application displays:

   * Resume match percentage
   * Matched skills
   * Missing skills
   * Extracted resume text

## 📊 Match Score Calculation

The application calculates the match percentage using the following formula:

```python
Match Score = (Matched Skills / Required Skills) * 100
```

For example:

* Required Skills: 5
* Matched Skills: 4
* Missing Skills: 1

**Match Percentage: 80%**

Note: The current implementation uses predefined keyword matching. It is not yet powered by a machine learning model or an external AI service, and the match percentage should not be treated as a validated ATS score.

## 📸 Screenshots

Add screenshots of your application here.

### Home Page

<!-- Add your home page screenshot here -->

### Resume Analysis Result

<!-- Add your result page screenshot here -->

## 🔮 Future Enhancements

* AI-powered resume analysis.
* More comprehensive skill extraction.
* Improved job description matching.
* Resume recommendations and improvement suggestions.
* Support for additional document formats.
* Advanced dashboard for analysis history.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Python full-stack development.
* Django application development.
* HTML, CSS, and JavaScript integration.
* PDF text extraction.
* Database operations using SQLite.
* Git and GitHub version control.
* Building a complete web application.

## 👨‍💻 Developer

**Narender Koyalkar Davke**

GitHub: https://github.com/narenderkoyalkardavke-tech

---

⭐ If you find this project interesting, feel free to star the repository!
