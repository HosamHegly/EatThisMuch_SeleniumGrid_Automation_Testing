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
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /B java -jar selenium-server.jar hub"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }

        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /B java -jar selenium-server.jar node --port 5555 --selenium-manager true"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }



        stage(' Running Tests') {
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