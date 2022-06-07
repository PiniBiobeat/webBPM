pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright/python:v1.22.0-focal'
    }
  }
  stages {
    stage('install playwright') {
      steps {
        sh '''
          pip install playwright
          playwright install --with-deps
        '''
      }
    }

    stage('test') {
      steps {
        sh '''
          pytest test_online_create_album.py
        '''
      }
      post {
        success {
          archiveArtifacts(artifacts: 'homepage-*.png', followSymlinks: false)
          sh 'rm -rf *.png'
        }
      }
    }
  }
}