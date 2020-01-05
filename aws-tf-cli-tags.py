import sys
import random
import os

def do_work():
   """ Function to handle command line usage"""
   args = sys.argv
   args = args[1:] # First element of args is the file name

   if len(args) == 0:
      print('You have not passed any commands in!')
   else:
      for a in args:
         if a == '--help':
            print('AWS: EC2 - S3 - List unused resources tool')
            print('Options:')
            print(' --help -> show this help menu.')
            print(' --ec2  -> show unused AWS resources in EC2.')
            print(' --s3   -> show unused AWS resources in S3')
            print(' --test -> test config with terraform')
         elif a == '--ec2':
            os.system("python unused_resources_aws2_ec2.py 1")
         elif a == '--s3':
            os.system("python unused_resources_aws_s3.py 1")
         elif a == '--test':
            os.system("cd terraform && terraform init && terraform plan && terraform apply -auto-approve && cd ..")
            os.system("python unused_resources_aws_ec2.py 1")
            os.system("cd terraform && terraform destroy -auto-approve")
         else:
            print('Unrecognised argument.')

if __name__ == '__main__':
   do_work()
