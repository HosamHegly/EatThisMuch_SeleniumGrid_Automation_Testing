pipeline {
    agent any
    stages {
        stage('Build') {
            steps {

                bat 'pip install -r requirements.txt' // Install dependencies if needed
            }
        }
         stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat 'py C:\Users\Hosam Hegly\PycharmProjects\eathThisMuchTesting\api_test_runner.py' // Replace with your test command
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}