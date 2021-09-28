#!groovy

pipeline {

    agent {
        docker { image 'xxx/xxxx:0.0.1' }
    }

    parameters {
        choice(
            name:'measured_environment',
            choices: ['test', 'prod', 'dev'],
            description: '被测环境')
    }

    environment {
        mail_to='123456789@qq.com'
    }

    options {
        buildDiscarder(
            logRotator(daysToKeepStr: '7', numToKeepStr: '10', artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10'))
    }

    triggers {
		cron('H 2 * * 1-5')
    }

    stages {
        stage('Prepare'){
            steps {
                script{
                    echo "被测环境：${params.measured_environment}"
                }
            }
        }
        stage('Test') {
            steps {
                script{
                    sh "pytest -n auto testcases --alluredir allure-results --env ${measured_environment}"
                    sh "allure generate allure-results --clean -o allure-report"
                    }
                }
            }
        }

    post {
        always {
            allure([
                disabled: false,
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-report/']]
                ])
            step([
                $class: 'Mailer',
                recipients: "${mail_to}",
                notifyEveryUnstableBuild: true,
                sendToIndividuals: true
                ])
            deleteDir()
        }
    }

}