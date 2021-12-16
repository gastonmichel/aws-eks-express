
from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
    aws_ecr_assets as ecr_assets,
)



class MissionDevEks(cdk.Stack):

    def __init__(
        self, scope: cdk.Construct, construct_id: str, 
        vpc: ec2.Vpc,
        **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        self.cluster = eks.Cluster(
            self, 'MissionDevEksCluster',
            cluster_name=self.node.try_get_context('k8s_cluster_name'),
            version=eks.KubernetesVersion.V1_21,
            vpc=vpc,
            vpc_subnets=[
                ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PUBLIC
                )
            ],
            default_capacity=1,
            default_capacity_instance=ec2.InstanceType('t3.small'),
        )

        self.cluster.aws_auth.add_user_mapping(
            user=iam.User.from_user_arn(
                self, 'rootUser',
                iam.AccountRootPrincipal().arn),
            groups=["system:masters"],
        )

        self.cluster.aws_auth.add_account(self.account)

