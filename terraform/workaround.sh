#!/bin/bash

AWSRegion=${1}

#get AWS public VPC subnets, zones
subnetzone1=`aws ec2 describe-subnets --subnet-ids ${PrivateSubnet1} --output text --region ${AWSRegion} | grep 'SUBNETS' | awk '{print $3}'`
echo "Zone1: ${subnetzone1}"

subnetzone2=`aws ec2 describe-subnets --subnet-ids ${PrivateSubnet2} --output text --region ${AWSRegion} | grep 'SUBNETS' | awk '{print $3}'`
echo "Zone2: ${subnetzone2}"

subnetzone3=`aws ec2 describe-subnets --subnet-ids ${PrivateSubnet3} --output text --region ${AWSRegion} | grep 'SUBNETS' | awk '{print $3}'`

echo ${PublicSubnet1} >> /opt/kops-state/KOPS_PUBLIC_SUBNETS
echo ${PublicSubnet2} >> /opt/kops-state/KOPS_PUBLIC_SUBNETS
echo ${PublicSubnet3} >> /opt/kops-state/KOPS_PUBLIC_SUBNETS

for i in `cat /opt/kops-state/KOPS_PUBLIC_SUBNETS`; 
do 
    echo $i; 
    zone=`aws ec2 describe-subnets --subnet-ids ${i} --output text --region ${AWSRegion} | grep 'SUBNETS' | awk '{print $3}'`;
    echo ${zone};

    for j in `aws elb describe-load-balancers --region ${AWSRegion} | grep "LoadBalancerName" | grep -v api | cut -d ':' -f 2 | cut -d '"' -f 2`; 
    do 
      echo "Adjust ELB: $j, attach to Subnet: $i ...";
      aws elb attach-load-balancer-to-subnets --load-balancer-name ${j} --subnets ${i} --region ${AWSRegion}
    done
done
