pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MansiBurud/student_enrollment_system.git'
            }
        }

        stage('Set up Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest discover'
            }
        }
    }

    post {
        success {
            echo '🎉 CI build successful!'
        }
        failure {
            echo '❌ CI build failed!'
        }
    }
}
