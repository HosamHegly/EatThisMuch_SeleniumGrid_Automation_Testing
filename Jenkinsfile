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

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python api_test_runner.py"
                            bat "docker rm api_test_runner"
                        },
                        'Add Food to Meal Test': {
                            bat "docker run --name performance_test ${IMAGE_NAME}:${TAG} python performance_test.py"
                            bat "docker rm performance_test"
                        }
                    )
                }
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
