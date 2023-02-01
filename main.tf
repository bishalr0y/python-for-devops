terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["~/.aws/credentials"]
}

# Create  ec2 instance
resource "aws_instance" "my_ec2_instance" {
  count         = 2 // number of instances
  ami           = "ami-06878d265978313ca"
  instance_type = "t2.micro"

  tags = {
    Name = "test-instance-name- ${count.index}"
  }
}