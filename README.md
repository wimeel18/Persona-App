# PersonaQuest – Personality Test Application

PersonaQuest is a desktop-based personality test application developed using Python, Kivy, and KivyMD. The application allows users to create an account, log in, and take an interactive MBTI (Myers-Briggs Type Indicator) personality test.

## 📌 About the Project

PersonaQuest was developed to provide users with a simple and interactive way to explore their personality preferences through an MBTI-style questionnaire.

The application combines a graphical user interface (GUI), user authentication, database management, and questionnaire-based scoring to deliver a personalized experience.

## ✨ Features

- **User Registration** — Allows new users to create an account.
- **User Login** — Provides account authentication using email and password.
- **Password Hashing** — Uses bcrypt to hash passwords before storing them in the database.
- **Personalized Dashboard** — Displays the logged-in user's name, current date, and motivational quotes.
- **Interactive MBTI Quiz** — Provides personality-related questions with a five-point response scale.
- **Paginated Questionnaire** — Displays questions in groups of 10 to make the test easier to navigate.
- **Automatic Score Calculation** — Calculates personality preferences across four MBTI dimensions:
  - Extraversion (E) / Introversion (I)
  - Sensing (S) / Intuition (N)
  - Thinking (T) / Feeling (F)
  - Judging (J) / Perceiving (P)

## 🛠️ Built With

- **Python** — Main programming language.
- **Kivy** — Framework for building the graphical user interface.
- **KivyMD** — Material Design components for the application interface.
- **SQLite** — Database management for user accounts.
- **Pandas** — Reading and processing questionnaire data from Excel.
- **Bcrypt** — Password hashing and authentication.

## 📂 Project Structure

```text
Persona-App/
│
├── main.py
│
├── cek_db.py
│
├── kv/
│   ├── hallog.kv
│   ├── daftar.kv
│   ├── beranda.kv
│   ├── quizmbti.kv
│   └── asset/
│       ├── excel/
│       ├── font/
│       └── ...
│
└── screens/
    ├── screen.py
    ├── hallog.py
    ├── daftar.py
    ├── beranda.py
    └── quizmbti.py
```

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your computer.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/wimeel18/Persona-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Persona-App
   ```

3. Install the required dependencies:

   ```bash
   pip install kivy kivymd pandas openpyxl bcrypt
   ```

### Configuration

Before running the application:

1. Make sure the MBTI questionnaire Excel file is available in `kv/asset/excel/`.
2. Configure the SQLite database path in the registration and login modules to match your local environment.
3. Ensure the required fonts and other assets are available in the project directory.

### Run the Application

Execute the following command:

```bash
python main.py
```

## 📖 How to Use

1. Open PersonaQuest.
2. Register a new account.
3. Log in using your registered email and password.
4. Explore the personalized dashboard.
5. Start the MBTI personality questionnaire.
6. Answer the questions using the available five-point response scale.
7. Complete all questionnaire pages.
8. View your calculated MBTI personality type.

## 🎯 Learning Objectives

This project was developed as part of an academic learning experience to apply programming concepts in building a desktop application.

Through this project, we explored:

- Python-based GUI development.
- Database integration using SQLite.
- User authentication and password security.
- Data processing using Pandas.
- Interactive questionnaire development.
- Basic scoring algorithms and logical data processing.

## 👩‍💻 Contributors

Developed as an academic group project.

---

*Discover yourself, one question at a time.*
