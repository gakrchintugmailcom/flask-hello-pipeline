pipeline {
    agent any

    stages {
        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 app.py
                '''
            }
        }
    }
}
