
# 💸 Expense Tracking System

A complete expense tracking system built with FastAPI and Streamlit. It allows users to record daily expenses, visualize them by category, and analyze trends over a date range.

---

## ✅ Features

- Add and update daily expenses with category and notes
- Automatically delete previous entries when updated
- Fetch expenses for specific dates
- Generate category-wise analytics with totals and percentages
- Fully dynamic rows in the frontend with Streamlit
- Display of formatted totals with two decimal points

---

## 🧰 Tech Stack

### Backend:
- Python
- FastAPI
- Pydantic
- MySQL
- mysql-connector-python

### Frontend:
- Streamlit
- Pandas
- Requests

---

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

### Step 1: Clone the repository:
   ```bash
   git clone https://github.com/uwajhi/expense-tracking-system.git
   cd expense-management-system
   ```
### Step 2: Install dependencies::   
   ```commandline
    pip install -r requirements.txt
   ```

### Step 3: MySQL Database Setup
```sql
CREATE DATABASE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    amount DECIMAL(10,2),
    category VARCHAR(255),
    notes TEXT
);
```
Update your `db_helper.py` to match your local database credentials.

---

## 🧾 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it with proper attribution.

---

## 🤝 Contributing

Contributions are welcome. Please fork the repository and create a pull request for any enhancements or bug fixes.

---

## 📬 Contact

If you have any questions or feedback, feel free to contact [usamawajhi.pk@gmail.com](mailto:usamawajhi.pk@gmail.com).
