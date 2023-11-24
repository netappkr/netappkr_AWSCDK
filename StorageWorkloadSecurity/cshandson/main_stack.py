from cshandson.NW_stack import NetworkStack
from cshandson.MSAD_stack import ADStack
from cshandson.bastion_stack import BastionStack

from cshandson.fsxn_stack import FSxNStack
from cshandson.BlueXP_req import BlueXPReqStack

from aws_cdk import (
    Stack,
    CfnParameter,
    Tags,
    Fn
    
)
from constructs import Construct

class mainStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Parameter
        prefix = CfnParameter(self, "prefix", type="String", default="netapp",
                              description="this parm use prefix or id in cfn. please input only english and all in lower case")
        creator = CfnParameter(self, "creator", type="String", default="netapp",
                              description="please insert you are name initial")
        
        # stack
        NW = NetworkStack(self, "NetworkStack", prefix=prefix)
        Tags.of(NW).add("creator", creator.value_as_string)

        BlueXP = BlueXPReqStack(self, "BlueXPReqStack", prefix=prefix)
        Tags.of(BlueXP).add("creator", creator.value_as_string)

        bastionhost = BastionStack(self, "BastionStack", vpc=NW.vpc, defaultsg=NW.defaultsg, prefix=prefix)
        Tags.of(bastionhost).add("creator", creator.value_as_string)
        bastionhost.add_dependency(NW)

        # DataBroker = DatabrokerStack(self, "DataBroker", vpc=NW.vpc, defaultsg=NW.defaultsg, prefix=prefix)
        # Tags.of(DataBroker).add("creator", creator.value_as_string)
        # DataBroker.add_dependency(bastionhost)
        
        # test = TestStack(self, "test", vpc=NW.vpc, defaultsg=NW.defaultsg, prefix=prefix)
        # Tags.of(test).add("creator", creator.value_as_string)
        # test.add_dependency(bastionhost)
        
        AD = ADStack(self, "ADStack", vpc=NW.vpc, prefix=prefix)
        Tags.of(AD).add("creator", creator.value_as_string)
        AD.add_dependency(NW)

        FSxN = FSxNStack(self, "FSxNStack", vpc=NW.vpc, AD=AD.cfn_microsoft_AD, defaultsg=NW.defaultsg, prefix=prefix)
        Tags.of(FSxN).add("creator", creator.value_as_string)
        FSxN.add_dependency(AD)







        