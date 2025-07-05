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

        stage('Free Port 5000') {
            steps {
                sh '''
                PORT=5000
                PID=$(lsof -ti :$PORT) || true
                if [ ! -z "$PID" ]; then
                    echo "Killing process using port $PORT: $PID"
                    kill -9 $PID
                fi
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
