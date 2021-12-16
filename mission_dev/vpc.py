
from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
    aws_ecr_assets as ecr_assets,
)


class MissionDevVpc(cdk.Stack):

    def __init__(
        self, scope: cdk.Construct, construct_id: str, 
        **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)


        self.vpc = ec2.Vpc(
            self, 'MissionDevK8sVpc',
            cidr='10.1.0.0/16',
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='PublicSubnet'
                )
            ]
        )
