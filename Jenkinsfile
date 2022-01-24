pipeline{
  agent any
  
  stages{
    stage('install boto3'){
      script{
        sh: "pip install boto3"
      }
    }
    stage('create'){
      parallel{
//         stage('produce'){
//           steps{
//             script{
//               dir('src'){
//                 sh "python3 producer.py"
//               }
//             }
//           }
//         }

        stage('produce kinesis stream'){
          steps{
            script{
              dir('src'){
                sh "python3 kinesis_producer.py"
              }
            }
          }
        }

        stage('produce kinesis consumer'){
          steps{
            script{
              dir('src'){
                sh "python3 kinesis_consumer.py"
              }
            }
          }
        }
//         stage('consume'){
//           steps{
//             script{
//               dir('src'){
//                 sh "python3 kinesis_consumer.py"
//               }
//             }
//           }
//         }
        
        
      }
    }
  }
}
