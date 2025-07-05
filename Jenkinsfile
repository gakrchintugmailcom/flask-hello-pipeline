pipeline {
    agent any

    environment {
        PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Free Port 5000') {
            steps {
                sh '''
                PID=$(lsof -t -i:$PORT || true)
                if [ ! -z "$PID" ]; then
                    echo "Killing process on port $PORT (PID: $PID)"
                    kill -9 $PID || true
                else
                    echo "No process running on port $PORT"
                fi
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
