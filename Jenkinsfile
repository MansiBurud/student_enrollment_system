pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Cloning from the main branch instead of master
                git branch: 'main', url: 'https://github.com/MansiBurud/student_enrollment_system.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'mvn clean install'  // For Windows
                // Or use sh 'mvn clean install' if on Linux
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'mvn test'
            }
        }

        stage('Archive') {
            steps {
                echo 'Archiving the build artifacts...'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build succeeded.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}

