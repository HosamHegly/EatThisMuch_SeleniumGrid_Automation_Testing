pipeline {
    agent any
    stages {
        stage('Build') {
            steps {

                pat 'pip install -r requirements.txt' // Install dependencies if needed
                checkout scm
                echo 'Building..'
            }
        }
         stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                pat 'python -m unittest test_pet.py' // Replace with your test command
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}