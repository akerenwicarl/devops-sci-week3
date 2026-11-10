pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // A virtual environment avoids "externally-managed-environment"
                // errors on newer Linux Jenkins agents.
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Unit Test') {
            steps {
                sh '.venv/bin/python -m pytest tests/ --junitxml=results.xml'
            }
        }
        stage('Regression Test') {
            steps {
                sh '.venv/bin/python scripts/run_regression.py'
            }
        }
        stage('Benchmark') {
            steps {
                sh '.venv/bin/python scripts/benchmark.py'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'results.xml'
            archiveArtifacts artifacts: 'benchmark.txt', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
