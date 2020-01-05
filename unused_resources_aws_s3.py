
import boto3
import os
from botocore.exceptions import ClientError

region = 'us-east-1'
ACCESS_ID = os.environ['AWS_ACCESS_KEY_ID']
ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
TAGSEARCH = os.environ['MY_TAG']
TAG_DEFAULT = 'nottagged'
TAG_VALUE = 'yes'
counter = 0

"""
A tool for retrieving basic information from the running S3 buckets.
"""

# Connect to S3
s3 = boto3.client('s3',
                  region,
                  aws_access_key_id=ACCESS_ID,
                  aws_secret_access_key= ACCESS_KEY)

#s3_re = boto3.resource('s3')

s3_re = boto3.resource('s3',
                     region,
                     aws_access_key_id=ACCESS_ID,
                     aws_secret_access_key= ACCESS_KEY)

print("================================\n")
print("Getting AWS S3 not tagged buckets WITH TAG NAME: %s" % TAGSEARCH)
print("=================================\n\n")

for bucket in s3_re.buckets.all():
    s3_bucket = bucket
    s3_bucket_name = s3_bucket.name
    bucket_tagging = s3_re.BucketTagging(s3_bucket_name)
    try:
        response = s3.get_bucket_tagging(Bucket=s3_bucket_name)
    except ClientError:
        #print (bucket+ ",does not have tags, add tag")
        #print("give key : ")
        #inp_key = input()
        #print("give value : ")
        #inp_val = input()
        response = bucket_tagging.put(
            Tagging={
                'TagSet': [
                    {
                        'Key': TAG_DEFAULT, 
                        'Value': TAG_VALUE
                    },
                ]
            }
        )
    # Get a list of all tags
    tag_set = response['TagSet']
    # Print out each tag
    for tag in tag_set: 
        if TAGSEARCH not in tag['Key']:
            print(tag) 
            print("================================\n")
            print("Instances without tag Id name detected: %s" % s3_bucket_name)
            print("=================================\n")      
            counter +=1  
    tag_set.clear() 
counterstr = int(counter)
print("================================\n")
print("Total instances detected without tag: %s " % counter )
print("================================\n")

