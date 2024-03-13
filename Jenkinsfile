pipeline {
    agent any

    environment {
        // Define environment variables if necessary
        CHROMEDRIVER_VERSION = 'latest'
    }

    stages {
        stage('Prepare Environment') {
            steps {
                checkout scm

                sh 'python3 -m pip install -r requirements.txt'

                sh """
                wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
                unzip chromedriver_linux64.zip
                export PATH=$PWD:$PATH
                """
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'python3 api_test_runner.py'
            }
        }

        stage('Run Add Food to Meal Tests') {
            steps {
                sh 'python3 add_food_to_meal_test_runner.py'
            }
        }
    }

    post {
        always {
            // Clean up Chromedriver
            sh 'rm -f chromedriver chromedriver_linux64.zip'

            // Add any post-build actions here
        }
    }
}
