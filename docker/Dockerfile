# Setup build arguments with default versions
ARG AWS_CLI_VERSION=1.17.9
ARG TERRAFORM_VERSION=0.12.2

# Download Terraform binary
FROM debian:stretch-20190506-slim as terraform
ARG TERRAFORM_VERSION
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl=7.52.1-5+deb9u9
RUN apt-get install -y unzip=6.0-21+deb9u2
RUN apt-get install -y gnupg=2.1.18-8~deb9u4
RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS
RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig
COPY hashicorp.asc hashicorp.asc
RUN gpg --import hashicorp.asc
RUN gpg --verify terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig terraform_${TERRAFORM_VERSION}_SHA256SUMS
RUN grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip terraform_${TERRAFORM_VERSION}_SHA256SUMS | sha256sum -c -
RUN unzip -j terraform_${TERRAFORM_VERSION}_linux_amd64.zip

#Aws-IAM-Authenticator
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator
RUN chmod +x ./aws-iam-authenticator
RUN mv aws-iam-authenticator /usr/local/bin/aws-iam-authenticator

#Aws-Heptio
RUN curl -o heptio-authenticator-aws https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.3.0/heptio-authenticator-aws_0.3.0_linux_amd64
RUN chmod +x heptio-authenticator-aws
RUN mv heptio-authenticator-aws /usr/local/bin/heptio-authenticator-aws

#Kubectl 
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv kubectl /usr/local/bin/kubectl

# Install AWS CLI using PIP
FROM debian:stretch-20190506-slim as aws-cli
ARG AWS_CLI_VERSION
RUN apt-get update
RUN apt -y install vim
RUN apt-get install -y python3=3.5.3-1
RUN apt-get install -y python3-pip=9.0.1-2+deb9u1
RUN pip3 install boto3 pprint awscli==${AWS_CLI_VERSION}


# Build final image
FROM debian:stretch-20190506-slim
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates=20161130+nmu1+deb9u1 \
    jq=1.5+dfsg-1.3 \
    python3=3.5.3-1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /usr/bin/python3 /usr/bin/python
COPY --from=terraform /terraform /usr/local/bin/terraform
COPY --from=terraform /usr/local/bin/aws* /usr/local/bin/
COPY --from=terraform /usr/local/bin/kube* /usr/local/bin/
COPY --from=aws-cli /usr/local/bin/aws* /usr/local/bin/
COPY --from=aws-cli /usr/local/lib/python3.5/dist-packages /usr/local/lib/python3.5/dist-packages
COPY --from=aws-cli /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages


WORKDIR /workspace
CMD ["bash"]
