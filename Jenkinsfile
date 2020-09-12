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
        sh '''ls
python3 -m pip install -r requirements.txt'''
      }
    }

  }
}