pipeline {
  agent any
  stages {
    stage('git-clone') {
      steps {
        git 'https://github.com/jkushnir/devops-project-2'
      }
    }

    stage('python-requirements') {
      steps {
        sh 'python3 -m pip install -r requirements.txt'
      }
    }

    stage('docker-compose-up') {
      steps {
        sh 'docker-compose up -d'
      }
    }

    stage('run-test') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE', message: 'Failed to retrieve scrore') {
          sh '''tests/e2e.py
echo "error code is $?"'''
        }

      }
    }

    stage('docker-compose-down') {
      steps {
        sh 'docker-compose down'
      }
    }

  }
}