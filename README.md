# 🧪 Automation Exercise Test Suite

**Auteur : Walid Khalfa**  
**Repository : [Walid-Khalfa/automation-exercise-tests](https://github.com/Walid-Khalfa/automation-exercise-tests)**

---

## 📌 Overview

This project contains a **comprehensive automated test suite** for [Automation Exercise](http://automationexercise.com), a demonstration e-commerce web application. It is built following **QA best practices** and industry standards to ensure **maintainability, scalability, and reliability**.

### Key Highlights

✅ **26 Test Cases** covering end-to-end user workflows  
✅ **Page Object Model (POM)** for maintainable test code  
✅ **Data-Driven Testing** with external data sources  
✅ **Continuous Integration** with GitHub Actions  
✅ **84% Pass Rate** (22/26 tests passing)  
✅ **Professional Test Reporting** with HTML artifacts  

---

## 📋 Table of Contents

1. [Project Structure](#-project-structure)
2. [Prerequisites](#-prerequisites)
3. [Installation & Setup](#-installation--setup)
4. [Running Tests](#-running-tests)
5. [Test Coverage](#-test-coverage)
6. [Current Status](#-current-status)
7. [CI/CD Pipeline](#-cicd-pipeline)
8. [Technologies](#-technologies)
9. [Troubleshooting](#-troubleshooting)
10. [Contributing](#-contributing)
11. [Contact](#-contact)

---

## 📁 Project Structure

```
automation-exercise-tests/
├── .github/
│   └── workflows/
│       └── test.yml                    # CI/CD automation
├── config/
│   └── settings.py                     # Environment & configuration
├── data/
│   ├── users.json                      # Test user data
│   └── payment_data.json               # Payment test data
├── pages/                              # Page Object Model
│   ├── base_page.py                    # Base class for all pages
│   ├── home_page.py
│   ├── signup_login_page.py
│   ├── account_creation_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_us_page.py
│   ├── test_cases_page.py
│   ├── category_page.py
│   └── brand_page.py
├── tests/                              # Test cases (26 total)
│   ├── conftest.py                     # pytest fixtures & hooks
│   ├── test_register_login.py          # User registration & login
│   ├── test_products_cart.py           # Product & cart functionality
│   ├── test_order_checkout.py          # Order & checkout flow
│   ├── test_contact_subscription.py    # Contact & newsletter
│   └── test_scrolling_categories_brands.py  # Navigation & filtering
├── utils/
│   ├── data_loader.py                  # Data loading utilities
│   └── helpers.py                      # Common helper functions
├── requirements.txt                    # Python dependencies
├── pytest.ini                          # pytest configuration
└── README.md
```

---

## 🔧 Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Python** | 3.11+ | Required for test execution |
| **pip** | Latest | Python package manager |
| **Git** | Optional | For cloning the repository |
| **Chromium** | Auto-installed | Installed via Playwright |

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Walid-Khalfa/automation-exercise-tests.git
cd automation-exercise-tests
```

### Step 2: Create a Virtual Environment

```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers

```bash
playwright install chromium
```

### Verify Installation

```bash
pytest --version
playwright --version
```

---

## 🚀 Running Tests

### Execute All Tests

```bash
# Verbose output (recommended for CI/CD)
pytest -v

# With headless mode (default)
pytest -v --headed=false
```

### Run Specific Test Suite

```bash
# User registration & login tests
pytest tests/test_register_login.py -v

# Product & cart tests
pytest tests/test_products_cart.py -v

# Order & checkout tests
pytest tests/test_order_checkout.py -v

# Contact & subscription tests
pytest tests/test_contact_subscription.py -v

# Navigation tests
pytest tests/test_scrolling_categories_brands.py -v
```

### Run Individual Test Case

```bash
pytest tests/test_register_login.py::test_tc1_register_user -v
```

### Execute Tests in Headed Mode (with Browser UI)

```bash
pytest --headed -v
```

### Generate HTML Report

```bash
pytest --html=report.html --self-contained-html -v
```

The report will be generated as `report.html` and can be viewed in any browser.

### Advanced Options

```bash
# Run tests in parallel (requires pytest-xdist)
pytest -v -n auto

# Stop on first failure
pytest -v -x

# Run only failed tests
pytest --lf -v

# Increase verbosity for debugging
pytest -vv --tb=long
```

---

## 📊 Test Coverage

### Test Cases by Category

#### 1. **User Registration & Login** (8 tests)
- TC1: Register new user
- TC2: Login with valid credentials
- TC3: Login with invalid credentials
- TC4: Logout user
- TC5: Register with existing email
- TC6: Register form validation
- TC7: Social login options
- TC8: Password reset functionality

#### 2. **Products & Cart** (6 tests)
- TC9: View all products
- TC10: Search products
- TC11: View product details
- TC12: Add product to cart
- TC13: Remove product from cart
- TC14: Update cart quantity

#### 3. **Order & Checkout** (5 tests)
- TC15: Proceed to checkout
- TC16: Verify checkout page
- TC17: Place order with payment
- TC18: Download invoice
- TC19: Continue shopping after order

#### 4. **Contact & Newsletter** (4 tests)
- TC20: Submit contact form
- TC21: Verify contact form validation
- TC22: Subscribe to newsletter
- TC23: Verify newsletter subscription

#### 5. **Navigation & Filtering** (3 tests)
- TC24: View categories
- TC25: Filter by brand
- TC26: Scroll through products

---

## 📈 Current Status

### Test Results Summary

| Metric | Value |
|--------|-------|
| **Total Tests** | 26 |
| **Passed** | 22 ✅ |
| **Failed** | 4 ❌ |
| **Success Rate** | 84% |
| **Last Run** | CI/CD Pipeline |

### Known Issues & Limitations

| Issue | Root Cause | Workaround | Status |
|-------|-----------|-----------|--------|
| Error message display inconsistency | Website variation on login/registration feedback | Soft assertion or visual validation | Investigation ongoing |
| Payment button timeout | Occasional network latency | Increase timeout threshold | In fix branch |
| Add to favorites (recommended items) | Requires additional hover interaction | Enhanced interaction logic | Pending |
| Form validation messages | Timing issue with element visibility | Added wait strategies | In fix branch |

**Fix Branch:** `fix/remaining-fails` (contains solutions for all 4 known issues)

---

## 🔁 CI/CD Pipeline

### GitHub Actions Workflow

The `.github/workflows/test.yml` file automates test execution on every `push` and `pull request` to the main branch.

### Pipeline Steps

1. **Code Checkout** – Clone repository
2. **Environment Setup** – Install Python 3.12
3. **Dependency Installation** – Install pip packages
4. **Browser Installation** – Download Chromium
5. **Test Execution** – Run pytest suite (headless mode)
6. **Report Generation** – Create HTML test report
7. **Artifact Upload** – Store report as GitHub artifact

### Accessing Pipeline Results

1. Navigate to **Actions** tab in GitHub repository
2. Click on the latest workflow run
3. View logs or download test report artifact

### Pipeline Status

- **Trigger Events:** `push`, `pull_request`
- **Target Branch:** `main`
- **Default Timeout:** 30 minutes
- **Artifact Retention:** 90 days

---

## 🛠️ Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Core language |
| **Playwright** | Latest | Browser automation & control |
| **pytest** | Latest | Test framework |
| **pytest-playwright** | Latest | Playwright integration |
| **Faker** | Latest | Random test data generation |
| **GitHub Actions** | N/A | CI/CD automation |
| **Chromium** | Latest | Target browser |

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### Issue: `ModuleNotFoundError: No module named 'playwright'`

**Solution:**
```bash
pip install -r requirements.txt
playwright install chromium
```

#### Issue: `TimeoutError` during test execution

**Solution:**
- Increase timeout in `config/settings.py`
- Check internet connection
- Run test individually: `pytest tests/test_name.py::test_case -v`

#### Issue: Playwright browser not found

**Solution:**
```bash
playwright install chromium
```

#### Issue: Tests fail on Windows with path errors

**Solution:**
- Use forward slashes `/` or raw strings in paths
- Ensure virtual environment is activated

#### Issue: Port conflicts in CI/CD

**Solution:**
- CI/CD uses headless mode by default (no port conflicts)
- Locally, run: `lsof -i :PORT_NUMBER` to identify conflicts

#### Issue: Test data not loading

**Solution:**
- Verify `data/` directory exists
- Check JSON syntax: `python -m json.tool data/users.json`
- Ensure file permissions are correct

### Debugging Tips

**Run with verbose logging:**
```bash
pytest -vv --tb=long tests/test_name.py
```

**Run with screenshots on failure:**
```bash
pytest tests/test_name.py --screenshot=only-on-failure
```

**Run with browser visible for inspection:**
```bash
pytest --headed tests/test_name.py
```

---

## 📝 Contributing

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/your-feature-name`
3. **Make your changes** following existing code patterns
4. **Add/update tests** for new functionality
5. **Run full test suite:** `pytest -v`
6. **Commit with clear messages:** `git commit -m "feat: add new test case for XYZ"`
7. **Push to branch:** `git push origin feature/your-feature-name`
8. **Open a Pull Request** with description of changes

### Code Standards

- **POM Pattern:** Always use Page Object Model for new pages
- **Naming:** Use descriptive test names: `test_tc{number}_{description}`
- **Comments:** Add docstrings to complex test methods
- **Data:** Externalize test data in JSON files
- **Assertions:** Use clear, specific assertions

### Before Submitting PR

- ✅ All tests pass locally (`pytest -v`)
- ✅ Code follows project structure
- ✅ New tests added for features
- ✅ README updated if necessary
- ✅ No hardcoded values in tests

---

## 📞 Contact

**Walid Khalfa**  
GitHub: [@Walid-Khalfa](https://github.com/Walid-Khalfa)  
Project: [automation-exercise-tests](https://github.com/Walid-Khalfa/automation-exercise-tests)

---

## 📄 License

This project is open source and available for educational and professional use.

---

## 🎉 Quick Start Command

```bash
# Clone, setup, and run tests
git clone https://github.com/Walid-Khalfa/automation-exercise-tests.git
cd automation-exercise-tests
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest -v
```

---

**Happy Testing! 🚀**
