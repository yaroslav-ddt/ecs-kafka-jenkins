pipeline{
  agent any 
  stages{
    stage('create'){
      parallel{
        stage('produce'){
          steps{
            script{
              dir('src'){
                sh "python3 producer.py"
              }
            }
          }
        }

        stage('consume'){
          steps{
            script{
              dir('src'){
                sh "python3 consumer.py"
              }
            }
          }
        }
        
       stage('ping'){
          steps{
            script{
              dir('src'){
                sh "ping kafka.test.yy"
              }
            }
          }
        }
        
      }
    }
  }
}
