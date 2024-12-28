## Getting Started

Install dependencies using pip

```bash
  pip install -r requirements.txt
```

> if you are on a different python version, for example python3.x you may have to replace `pip` with `pip3`

## Run Automated Tests

Run all tests without using Allure Rpeport

```bash
  pytest --browser=<browser_name> --html logs/report.html src/
```

## Execute a specific example

To run a specific Selenium Python example, use the following command:

```bash
  pytest --browser=<browser_name> --html logs/report.html path/to/test_script.py
```

Make sure to replace `path/to/test_script.py` with the path and name of the example you want to run.

## Run Using IDE

You just need to choose one of the tests from "tests" directory and click "Run test" green arrow.

## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --browser=<browser_name> --alluredir <reports_directory_path> src/
```
After that you need to use command:
```
$ allure serve <reports_directory_path>
```
Report is generated in Chrome browser.
