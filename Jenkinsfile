pipeline{
  agent any
  environment {
    AWS_ACCESS_KEY_ID = "AKIAXCE425KHXXQOLGBA"
    AWS_SECRET_ACCESS_KEY = "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" 
  }
  
  stages{
    stage('aws credentials'){
      
    }
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

        stage('produce kinesis stream'){
          steps{
            script{
              dir('src'){
                sh "python3 kinesis_producer.py"
              }
            }
          }
        }
//         stage('consume'){
//           steps{
//             script{
//               dir('src'){
//                 sh "python3 consumer.py"
//               }
//             }
//           }
//         }
        
        
      }
    }
  }
}
