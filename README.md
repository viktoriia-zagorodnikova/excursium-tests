# 🎟️ Automated Tests for Excursium

**Tech stack:** Python · Selenium WebDriver · Pytest

> ⚠️ **Note:** This is a personal pet project built to practice test automation skills. It is not affiliated with or endorsed by Excursium.

## 📋 Project Description

Automated test suite for the Excursium excursion booking website front-end (https://excursium.com/).

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Pytest | Test framework for running and organizing tests |
| Selenium WebDriver | Browser automation |

## 🤔 Why These Tools

- **Selenium** was chosen for Chrome browser automation — it simulates real user actions such as clicks, text input, and navigation.
- **Pytest** was chosen for organizing and running tests — clean structure, readable reports.
- **Python** was chosen as the main language — simple syntax, strong support for Selenium and Pytest.

## 🗂 Project Structure

```
excursium_tests/
├── conftest.py             # driver setup and teardown
├── tests/
│   ├── test_auth.py        # login tests (EX-001, EX-002)
│   ├── test_register.py    # registration tests (EX-009, EX-013)
│   └── test_filter.py      # filtering tests (EX-014, EX-017)
└── requirements.txt        # dependencies
```

## ✅ What's Covered

- Login with email and password
- New user registration
- Filters on the excursions page

  Known limitation: the site has anti-bot protection that may occasionally interrupt automated test runs with a "suspicious activity" verification page. If a test fails unexpectedly, try re-running it.

## 🔗 Site

[excursium.com](https://excursium.com/)
