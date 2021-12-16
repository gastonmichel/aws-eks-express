# Express sample app on EKS cluster

Requirements:

1. docker installed
1. aws-cli installed and configured
1. cdk installed
1. python installed
1. kubectl installed

## Setup the environment:

Define the aws account to deploy:

    CDK_ACCOUNT=<account>

Define the aws region to deploy:

    CDK_REGION=<region>

Define the kubeconfig temp location:

    KUBECONFIG=/tmp/.kube/config

Install the dependencies:

    pip install -r requirements.txt

Bootstrap the cdk:

    cdk bootstrap aws://$CDK_ACCOUNT/$CDK_REGION

## Deploy the app

Deploy the vpc stack:

    cdk deploy MissionDevVps

Deploy the eks stack:

    cdk deploy MissionDevEks 

Deploy the image stack:

    cdk deploy MissionDevImage

Copy the image name from the stack output and paste it in the container image placeholder at `express-sample-app/deployment.yaml`

Get the kubeconfig:

    aws eks update-kubeconfig --name mission-dev --region $CDK_REGION

Test the kubeconfig credentials

    kubectl --kubeconfig $KUBECONFIG get ns

Apply the template:

    kubectl --kubeconfig $KUBECONFIG apply -f express-sample-app/deployment.yaml

## Test the app

Port-forward into the sample app:

    kubectl --kubeconfig $KUBECONFIG port-forward service/express-app 3000:3000

Test the app is working:

    curl localhost:3000

## Destroy the resources

To destroy the resources run: 

    cdk destroy --all