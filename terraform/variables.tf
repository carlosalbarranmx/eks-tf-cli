variable "aws_region" {
 type = "string"
 description = "Used AWS Region."
 default     = "{{env `AWS_DEFAULT_REGION`}}" 
}
variable "aws_access_key" {
 type = "string"
 description = "The account identification key used by your Terraform client."
 default     = "{{env `AWS_ACCESS_KEY_ID`}}"
}
variable "aws_secret_key" {
 type = "string"
 description = "The secret key used by your terraform client to access AWS."
 default     = "{{env `AWS_SECRET_ACCESS_KEY`}}"
}

variable "subnet_count" {
    type        = "string"
    description = "The number of subnets we want to create per type to ensure high availability."
}

variable "accessing_computer_ip" {
 type = "string"
 description = "IP of the computer to be allowed to connect to EKS master and nodes."
}

variable "keypair-name" {
  type = "string"
  description = "Name of the keypair declared in AWS IAM, used to connect into your instances via SSH."
}

variable "hosted_zone_id" {
  type = "string"
  description = "ID of the hosted Zone created in Route53 before Terraform deployment."
}

variable "hosted_zone_url" {
  type = "string"
  description = "URL of the hosted Zone created in Route53 before Terraform deployment."
}
