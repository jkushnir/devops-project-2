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
        sh 'tests/e2e.py'
      }
    }

  }
}