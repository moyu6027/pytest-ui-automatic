#!/usr/bin/env bash
echo "-> Installing dependencies"
python3 -m pip install --upgrade pip
python3 -m pip install pipenv
#python3 -m playwright install
pipenv install
npm i cucumber-html-reporter

#echo "-> Removing old Allure results"
#rm -r allure-results/* || echo "No results"

echo "-> Start tests"
pipenv run pytest -n auto tests/ --cucumber-json=bdd-report/cucumber-report.json --base-url http://automationpractice.com --reportportal
echo "-> Test finished"

echo "-> Generating report"
#cp environment.properties allure-results/
node bdd-report/generate-html-report.js
echo "-> Open report"
#allure open allure-report/