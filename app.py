#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from mission_dev.vpc import MissionDevVpc
from mission_dev.eks import MissionDevEks
from mission_dev.image import MissionDevImage



app = cdk.App()

env = cdk.Environment(
    account=os.getenv('CDK_ACCOUNT'),
    region=os.getenv('CDK_REGION')
)

network = MissionDevVpc(
    app, 'MissionDevVpc', env=env,
)

cluster = MissionDevEks(
    app, 'MissionDevEks', env=env,
    vpc=network.vpc,
)

image = MissionDevImage(
    app, 'MissionDevImage', env=env,
)

app.synth()
