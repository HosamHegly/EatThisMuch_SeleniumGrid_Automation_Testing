pipeline {
    agent any



    stages {
        stage('Setup Environment') {
            steps {
                echo '$path'
                echo 'Setting up Python environment...'
                bat 'C:\\Python\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe check_macro_calories_validity_test_runner.py"
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