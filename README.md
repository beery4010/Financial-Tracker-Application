# 💰 Financial Tracker Application

A command-line based **Personal Finance Tracker** built in Python with a clean, modular architecture. Track your income and expenses, manage transaction records, and generate financial reports all from the terminal.

---

## 📌 Features

- ➕ Add income and expense transactions
- 📋 View and manage transaction history
- 📊 Generate financial summary reports
- 🗂️ Persistent CSV-based data storage
- 🛡️ Custom exception handling for robust error management
- 📝 Built-in logging system to track application events

---

## 🗂️ Project Structure

```
Financial Tracker Application/
│
├── main.py                  # Entry point of the application
├── test.ipynb               # Jupyter Notebook for testing and exploration
├── user_instruction.txt     # instructions
│
├── Data/
│   └── recordData.csv       # Persistent storage for all transactions
│
├── Logs/
│   └── log.log              # Application event and error logs
│
└── Tracker/
    ├── __init__.py
    ├── transaction.py       # Transaction creation and management
    ├── record_data.py       # CSV read/write operations
    ├── reporting.py         # Financial summary and report generation
    ├── exceptions.py        # Custom exception classes
    ├── logger.py            # Logging configuration and setup
    └── utils.py             # Helper/utility functions
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10 | Core language |
| CSV | Data persistence |
| OOP | Modular design |
| Logging module | Event tracking |
| Jupyter Notebook | Testing & exploration |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/beery4010/Financial-Tracker-Application.git

# Navigate into the project directory
cd financial-tracker-application
```

### Run the Application

```bash
python main.py
```

---

## 📖 How to Use

Once you run `main.py`, you will be presented with a menu-driven CLI interface. Follow the on-screen prompts to:

1. **Add a Transaction** — Enter details like type (income/expense), amount, category, and date
2. **View Records** — Browse all saved transactions
3. **Generate Report** — Get a summary of your income, expenses, and net balance
4. **Exit** — Safely close the application

---

## 📄 License

This project is open source and available under the MIT License.
