# eks-tf-cli
Create a complete EKS cluster (AWS cli&amp; Dockerfile) with Terraform and deploy a flask service - Unit Tests with Python - Tiny command line utility. 

Steps to run and test the automation:

### Build Dockerfile and tag it:
```
$ cd docker
$ docker build -t "eks-terraform-cli:1.2" . 
```
### Modify aws-terraform-cli.env with the correct values from AWS.
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY 
AWS_DEFAULT_REGION
```

### Run the Docker image:
```
$docker run -it -v ${PWD}:/workspace --env-file ./docker/aws-terraform-cli.env eks-terraform-cli:1.2
```

## Run the tool from the command line inside the container and select the correct option:
```
$python ./eks-tf-cli-tags.py
 
AWS - EKS - Terraform : Demo Tool
Options:
 --help       -> show this help menu.
 --tf         -> execute terraform validate and apply.
 --passtest   -> pass unit test - flask deployment
 --failtest   -> fail unit test - flask deployment
 --prepare    -> prepare tests

```

e) The correct execution steps are: tf, prepare and then passtest or failtest.

## Authors

* **Carlos Albarran**

