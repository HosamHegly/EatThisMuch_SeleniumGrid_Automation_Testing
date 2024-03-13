pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'my_tests_jenkins'
        TAG = 'latest' // You can also use a build ID or any other tag
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${IMAGE_NAME}:${TAG}", '.')
                }
            }
        }

        stage('Run API Test') {
            steps {
                script {
                    // Run the Docker container to execute api_test_runner.py
                    docker.run("${IMAGE_NAME}:${TAG}", "python api_test_runner.py")
                }
            }
        }

        stage('Run Add Food to Meal Test') {
            steps {
                script {
                    // Run the Docker container to execute add_food_to_meal_test_runner.py
                    docker.run("${IMAGE_NAME}:${TAG}", "python add_food_to_meal_test_runner.py")
                }
            }
        }
    }

    post {
        always {
            // This could be used to clean up Docker images, for example
            echo 'Cleaning up...'
            sh "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}