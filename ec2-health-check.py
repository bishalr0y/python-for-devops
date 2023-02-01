import boto3

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

# instace state
reservations = ec2_client.describe_instances()
#print(reservations)

print("-----INSTANCE STATE-----")
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        instance_state = instance['State']['Name']
        instance_id = instance['InstanceId']
        
        print(f"Instance {instance_id} is {instance_state}")
        

# status check
print("-----STATUS CHECK-----")
response = ec2_client.describe_instance_status()
instance_statuses = response['InstanceStatuses']
for instance_status in instance_statuses:
    ins_status = instance_status['InstanceStatus']['Status']
    sys_status = instance_status['SystemStatus']['Status']
    print(f"Instance {instance_status['InstanceId']} instance status is {ins_status} and system status is {sys_status}")