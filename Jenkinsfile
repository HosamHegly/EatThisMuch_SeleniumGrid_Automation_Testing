pipeline {
    agent any



    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Python\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /b java -jar selenium-server-4.17.0.jar hub"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }

        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }



        stage(' Running Tests') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python api_test_runner.py"
                            bat "docker rm api_test_runner"
                        },
                        'Add Food to Meal Test': {
                            bat "docker run --name add_food_to_meal_test_runner ${IMAGE_NAME}:${TAG} python add_food_to_meal_test_runner.py"
                            bat "docker rm add_food_to_meal_test_runner"
                        }
                    )
                }

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