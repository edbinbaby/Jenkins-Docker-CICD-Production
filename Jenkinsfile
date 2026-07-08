pipeline {

agent any

stages {


stage('Build Image') {

steps {

sh 'docker build -t devops-app .'

}

}


stage('Deploy Production') {

steps {

sh '''

docker save devops-app > app.tar


scp -i /var/jenkins_home/EdbinBaby.pem \
-o StrictHostKeyChecking=no \
app.tar ubuntu@172.31.26.159:/home/ubuntu/


ssh -i /var/jenkins_home/EdbinBaby.pem \
-o StrictHostKeyChecking=no \
ubuntu@172.31.26.159 "

docker load < /home/ubuntu/app.tar

docker stop app || true

docker rm app || true

docker run -d \
--name app \
-p 5000:5000 \
devops-app

"

'''

}

}


}

}
