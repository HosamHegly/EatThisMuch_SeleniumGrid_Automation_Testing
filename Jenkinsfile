pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
//                 sh 'python -m pip install --upgrade pip'
                bat 'C:\\Users\\Hosam Hegly\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip install -r requirements.txt'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add test execution steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
//                 git 'commit -am "Deploying latest changes"'
//                 git 'push origin main'

            }
        }
    }
}