import boto3
import sys


class AwsEC2Lab(object):

    def __init__(self):
        """ aws resource type :- ec2 """
        self.ec2 = ec2 = boto3.resource('ec2')

    def create_ec2_instance(self):
        """create free-tier image"""
        instance = self.ec2.create_instances(
            ImageId='ami-922914f7',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'
        )
        print 'created process id=:', instance[0].id
        instance_id = instance[0].id
        return instance_id

    def list_all_instances(self):
        """list all ec2 instances"""
        for instance in self.ec2.instances.all():
            id = instance.id
            state = instance.state
            print "id =:{} state {}".format(id,state)
            return "id =:{} state {}".format(id,state)

    def terminate_instance(self, instance_id=None):
        """ terminate instance """
        if not instance_id:
            return False

        print 'instance_id ={}'.format(instance_id)
        instance = self.ec2.Instance(instance_id)
        response = instance.terminate()
        return response

class AWS3Lab(object):

    def __init__(self):
        """ aws resource type :- s3 """
        self.s3 = boto3.resource('s3')

    def list_bucket_content(self):
        """ list all bucket objects """
        for bucket in self.s3.buckets.all():
            print 'bucket_name={}'.format(bucket.name)
            print "---"
            for item in bucket.objects.all():
                print "\t%s" % item.key

    def put_file_into_bucket(self, bucket_name, object_name):
        """ put file in bucket """
        try:
            response = self.s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'))
            return response
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    aws_ec2 = AwsEC2Lab()
    # print aws.create_ec2_instance()

    # list all instances
    aws_ec2.list_all_instances()
    # response = aws_ec2.terminate_instance('i-0f3ff1a1bd60c11ef')

    # s3 bucket objects
    aws_s3 = AWS3Lab()
    aws_s3.put_file_into_bucket('angautam-aws-s3-bucket', 'aws-python-lab-1.py')

    # list all bucket objects
    print aws_s3.list_bucket_content()



