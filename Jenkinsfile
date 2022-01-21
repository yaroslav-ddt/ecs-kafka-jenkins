pipeline {
  agent any 
  stages {
    stage('create') {
      parallel{
        stage {
          steps{
              dir('src'){
                sh "python3 producer.py"
              }
          }
        }

        stage {
          steps{
            script{
              dir('src'){
                sh "python3 consumer.py"
              }
            }
          }
        }
      }
    }
  }
}
