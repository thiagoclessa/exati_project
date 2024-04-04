terraform {
  backend "s3" {
    bucket = "exati-teste"
    key    = "exati-ec2-demo/terraform.tfstate"
    region = "us-east-1"
  }
}