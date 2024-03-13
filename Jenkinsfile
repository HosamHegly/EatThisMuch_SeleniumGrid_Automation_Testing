pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest' // You can also use a build ID or any other tag
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                // Run the Docker container to execute api_test_runner.py
                bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python api_test_runner.py"
                // Cleanup
                bat "docker rm api_test_runner"
            }
        }

        stage('Run Add Food to Meal Test') {
            steps {
                // Run the Docker container to execute add_food_to_meal_test_runner.py
                bat "docker run --name add_food_to_meal_test_runner ${IMAGE_NAME}:${TAG} python add_food_to_meal_test_runner.py"
                // Cleanup
                bat "docker rm add_food_to_meal_test_runner"
            }
        }
    }

    post {
        always {
            // This could be used to clean up Docker containers and images
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}
