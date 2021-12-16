
from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
    aws_ecr_assets as ecr_assets,
)

    
class MissionDevImage(cdk.Stack):

    def __init__(
        self, scope: cdk.Construct, construct_id: str, 
        **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        self.image = ecr_assets.DockerImageAsset(
            self, 'MissionDevExpressImage',
            directory='./express-sample-app',
        )

        cdk.CfnOutput(
            self, 'ImageURI',
            value=self.image.image_uri
        )

