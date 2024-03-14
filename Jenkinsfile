pipeline {
    agent any

    environment {
        PIP_PATH = 'C:\\Python\\Python312\\Scripts\\pip.exe'
        PYTHON_PATH = 'C:\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
//                 bat "${PYTHON_PATH} -m venv venv"
//                 bat "${PYTHON_PATH} -m pip install --upgrade pip"
                bat "${PIP_PATH} install -r requirements.txt"
            }
        }



        stage('running ui test') {
            steps {
                echo 'Testing..'
                bat "${PYTHON_PATH}  check_macro_calories_validity_test_runner.py"
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