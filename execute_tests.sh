#!/usr/bin/env bash
source venv/bin/activate
echo "-> Installing dependencies"
python3 -m pip install --upgrade pip
python3 -m playwright install
pip3 install -r requirements.txt --quiet

echo "-> Removing old Allure results"
rm -r allure-results/* || echo "No results"

echo "-> Start tests"
export BASE_URL=http://172.17.162.166:35041
pytest -n auto tests/test_login_page.py --alluredir allure-results --headed --base-url http://172.17.162.166:35041
# --base-url http://automationpractice.com --headed
echo "-> Test finished"

echo "-> Generating report"
cp environment.properties allure-results/
allure generate allure-results --clean -o allure-report
echo "-> Execute 'allure serve' in the command line"

echo "-> Open report"
#allure open allure-report/