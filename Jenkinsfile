pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python api_test_runner.py"
                bat "docker rm api_test_runner"
            }
        }

        stage('Run Add Food to Meal Test') {
            steps {
                bat "docker run --name add_food_to_meal_test_runner ${IMAGE_NAME}:${TAG} python add_food_to_meal_test_runner.py"
                bat "docker rm add_food_to_meal_test_runner"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}
