import boto3
import pytest

# Create a boto3 client for EC2 servicee
#ec2 = boto3.client('ec2',aws_access_key_id="AKIAZTPX3VCS4H6BJPHZ",aws_secret_access_key="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", region_name='us-east-1')


#@pytest.fixture
def test_vpc():
    ec2 = boto3.client('ec2',aws_access_key_id="AKIAZTPX3VCS4H6BJPHZ",aws_secret_access_key="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", region_name='ap-south-1')

    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16',
                         TagSpecifications=[
                             {
                                 'ResourceType': 'vpc',
                                 'Tags': [
                                     {
                                         'Key': 'Name',
                                         'Value': 'VPC03'
                                     },
                                 ],
                             },
                         ])
    VpcId=vpc['Vpc']['VpcId']
    print(VpcId)
    response = ec2.describe_vpcs(VpcIds=[VpcId])
    print(response)