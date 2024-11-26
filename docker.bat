


powershell docker build -t survey .
powershell docker tag survey:latest 110343760835.dkr.ecr.eu-west-1.amazonaws.com/survey:latest
powershell docker push 110343760835.dkr.ecr.eu-west-1.amazonaws.com/survey:latest