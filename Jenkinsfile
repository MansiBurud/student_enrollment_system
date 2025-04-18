pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git 'https://github.com/MansiBurud/student_enrollment_system.git'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 Building the project...'
                sh 'mvn clean install'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh 'mvn test'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo '📦 Archiving...'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Build passed!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
