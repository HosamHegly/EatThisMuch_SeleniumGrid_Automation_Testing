pipeline {
    agent any



    stages {
        stage('Set Python Env') {
            steps {
                bat '''
                    py -m venv venv
                 '''
                    }
                    }

        stage('Build') {
            steps {
                echo 'Building..'
                pip install -r requirements.txt            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat "python api_test_runner.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rd /s /q venv"
        }

        success {
            echo 'Build succeeded.'
            // Additional steps for successful build
        }

        failure {
            echo 'Build failed.'
            // Additional steps for failed build
        }
    }
}