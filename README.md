# aws-terraform-tags
List AWS Resources (EC2 &amp; S3) by tag - Command Line Tool (Python) - Tests with Terraform 

Steps to run and test the automation:

###Build Dockerfile and tag it:
```
$ cd docker
$ docker build -t "aws-terraform-cli:1.2" . 
```
###Modify aws-terraform-cli.env with the correct values from AWS, also set the value for MY_TAG. This is the target tag.
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY 
MY_TAG
```

###Run the Docker image:
```
$docker run -it -v ${PWD}:/workspace --env-file ./docker/aws-terraform-cli.env aws-terraform-cli:1.2
```

##Run the tool from the command line inside the container and select the correct option:
```
$python ./aws-tf-cli-tags.py
 
AWS: EC2 - S3 - List unused resources tool
Options:
 --help -> show this help menu.
 --ec2  -> show unused AWS resources in EC2.
 --s3   -> show unused AWS resources in S3
 --test -> test config with terraform
```

e) Get the results.

## Authors

* **Carlos Albarran**

