# **play_with_playwright**

A lightweight Python project demonstrating **web UI automation with Playwright**, **data-driven testing using Excel**, and **pytest fixtures/page-object patterns**.
This repository is ideal for beginners learning Playwright with Python, or anyone exploring structured test automation frameworks.

---

## **📁 Project Structure**

```
play_with_playwright/
│
├── data/
│   └── test_data.xlsx           # Excel file containing test input data
│
├── pages/
│   ├── base_page.py             # Shared base class for all page objects
│   └── form_page.py             # Page object for interacting with a sample form
│
├── tests/
│   └── test_form_excel.py       # Test reading Excel data + filling form via Playwright
│
├── fixtures/
│   └── browser_fixture.py       # Pytest fixture configuring Playwright browser context
│
├── utils/
│   └── excel_reader.py          # Utility module for reading Excel files
│
├── pytest.ini                   # Pytest configuration
└── requirements.txt             # Python dependencies
```

---

## **✨ Features**

* ✔️ **Playwright for Web UI automation**
* ✔️ **Page Object Model (POM)** for clean and maintainable test code
* ✔️ **Excel-driven test data** (via `openpyxl` or similar library)
* ✔️ **Reusable pytest fixtures** for browser lifecycle
* ✔️ **Example form automation test** reading multiple rows from Excel

---

## **🔧 Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/yourname/play_with_playwright.git
   cd play_with_playwright
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:

   ```bash
   playwright install
   ```

---

## **▶️ Running Tests**

Run all tests:

```bash
pytest
```

Run with headed browser mode:

```bash
pytest --headed
```

Run a specific test:

```bash
pytest tests/test_form_excel.py
```

---

## **📘 How It Works**

### **1. Excel Data → Test Logic**

`utils/excel_reader.py` loads test rows from `data/test_data.xlsx`.
Each row is passed as input into the test.

### **2. Page Objects**

* `base_page.py` provides common functions such as navigation, element handling, etc.
* `form_page.py` implements actions for a specific web form.

### **3. Browser Fixture**

`browser_fixture.py` creates a browser/page instance so tests remain clean and modular.

### **4. Tests**

`test_form_excel.py` iterates through Excel rows and fills out the form for each dataset.

---

## **📦 Requirements**

See `requirements.txt`, typically including:

* `playwright`
* `pytest`
* `openpyxl` (if reading Excel)
* other utility libraries as needed

---

## **🤝 Contributing**

Pull requests are welcome! If you’d like to add features, contribute enhancements, or improve documentation, feel free to fork and submit a PR.

---

## **📄 License**

MIT.

---
