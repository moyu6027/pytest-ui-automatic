var reporter = require('cucumber-html-reporter');

var options = {
        theme: 'bootstrap',
        jsonFile: 'bdd-report/cucumber-report.json',
        output: 'bdd-report/cucumber_report.html',
        reportSuiteAsScenarios: true,
        scenarioTimestamp: true,
        launchReport: true,
        name: 'Pytest-ui-automatic Report',
        brandTitle: 'Pytest BDD Report',
        metadata: {
            "App Version":"1.0.0",
            "Test Environment": "STAGING",
            "Browser": "Chrome  94.0.4595.0",
            "Platform": "Mac",
            "Parallel": "Scenarios",
            "Executed": "Remote"
        }
    };

    reporter.generate(options);