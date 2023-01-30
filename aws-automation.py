import boto3

client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region="us-east-1")


# creating vpc
new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)
new_vpc.create_tags(
    Tags = [
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)

# lists all avaiable VPCs
all_avaialable_vpcs = client.describe_vpcs() # returns a dictionary

vpcs = all_avaialable_vpcs['Vpcs']

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_association_set = vpc["CidrBlockAssociationSet"]
    
    for assoc_set in cidr_block_association_set:
        print(assoc_set["CidrBlockState"])
        
        
