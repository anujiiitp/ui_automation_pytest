🧪 UI Automation Framework with Python & Pytest
This repository contains a robust UI automation framework built from scratch using Python and Pytest, designed to improve scalability, maintainability, and reusability of automated UI tests. The framework is structured using the Page Object Model (POM) to encapsulate UI components and actions, making it clean, modular, and easy to extend.

📌 Features
✅ Built with Pytest for simple yet powerful test execution

🧱 Page Object Model (POM) structure for better test modularity and readability

📸 Automatic Screenshot Capture on test failures to aid quick debugging

🧾 HTML Test Reports generated after each run for easy result visualization

⚙️ Customizable Test Configuration using pytest.ini and command-line options

📁 Organized Folder Structure for reports, screenshots, and test artifacts

🗂️ Project Structure
ui-automation-framework/
│
├── pages/                  # Page classes representing web pages
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/                  # Test cases organized by functionality
│   └── test_login.py
│
├── utils/                  # Utility functions (e.g., screenshot logic)
│   └── helpers.py
│
├── reports/                # HTML reports of test runs
│
├── screenshots/            # Failure screenshots (auto-generated)
│
├── conftest.py             # Pytest fixtures and hooks
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration file
└── README.md               # Project documentation
