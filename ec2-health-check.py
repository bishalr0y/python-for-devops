import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

def health_check():

    # instance state
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
        
        
        
        
if __name__ == "__main__":
    # schedule.every(5).minutes.do(health_check) # to run every 5 minutes
    schedule.every(6).seconds.do(health_check) # to run every 6 seconds
    # schedule.every().wednesday.at("13:15").do(health_check)
    # schedule.every().day.at("10:30").do(health_check)
    # schedule.every(5).to(10).minutes.do(health_check)
    
    
while True:
    schedule.run_pending() # this will run the script