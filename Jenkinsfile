pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                 bat '''
                    py -m venv venv
                    venv\\Scripts\\activate.bat
                '''
//                 sh 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'


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

