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
            print('AWS - EKS - Terraform : Demo Tool')
            print('Options:')
            print(' --help       -> show this help menu.')
            print(' --tf         -> execute terraform validate and apply.')
            print(' --passtest   -> pass unit test - flask deployment')
            print(' --failtest   -> fail unit test - flask deployment')
            print(' --prepare    -> prepare tests')
         elif a == '--passtest':
            os.system("python python_test.py")
         elif a == '--failtest':
            os.system("python python_test_fail.py")
         elif a == '--tf':
            os.system("cd terraform && terraform validate && terraform apply -auto-approve && cd ..")
         elif a == '--prepare':
            os.system("aws eks update-kubeconfig --name flugeldev-cluster && kubectl delete -f curl.yml && kubectl apply -f curl.yml")
         else:
            print('Unrecognised argument.')

if __name__ == '__main__':
   do_work()
