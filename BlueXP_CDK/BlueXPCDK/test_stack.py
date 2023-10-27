from aws_cdk import aws_directoryservice as directoryservice
from aws_cdk import NestedStack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import Fn
from aws_cdk import CfnParameter
from aws_cdk import CfnOutput
from aws_cdk import cloudformation_include as cfn_inc
from constructs import Construct


class TestStack(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, vpc, defaultsg, prefix, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpcid=vpc.vpc_id
        keyPairname=Fn.import_value("keypairname")
        #vpc_subnet="subnet-0e72210d0504f2286"
        #vpc_subnet=Fn.join(delimiter='',list_of_values=[vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnet_ids[0]])
        vpc_subnet=vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnet_ids[0]
        BrokerEC2Role=Fn.import_value("DataBrokerRoleName")
        template = cfn_inc.CfnInclude(self, "test", template_file="test.json",
                                        parameters=dict(
                                            VpcId=vpcid,
                                            KeyPair=keyPairname,
                                            SubnetId=vpc_subnet
                                        ))

