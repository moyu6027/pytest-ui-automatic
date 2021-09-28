#!/usr/bin/env bash
source venv/bin/activate
echo "-> Installing dependencies"
python3 -m pip install --upgrade pip
python3 -m playwright install
pip3 install -r requirements.txt --quiet
#
#echo "-> Removing old Allure results"
#rm -r allure-results/* || echo "No results"

echo "-> Start tests"
pytest -n auto tests/step_definition/ --cucumber-json=bdd-report/cucumber-report.json --base-url http://automationpractice.com --headed
echo "-> Test finished"

echo "-> Generating report"
node bdd-report/generate-html-report.js

echo "-> Open report"
#allure open allure-report/