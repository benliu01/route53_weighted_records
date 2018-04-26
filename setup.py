from setuptools import setup

setup(
  name = 'route53weightedrecords',
  packages = ['route53weightedrecords'],
  version = '0.4',
  description = 'Python package to manage over 100 weighted records in AWS Route53.',
  author = 'Benjamin Liu',
  author_email = 'ben@mightysignal.com',
  url = 'https://github.com/benliu01/route53_weighted_records',
  download_url = 'https://github.com/benliu01/route53_weighted_records/archive/0.4.tar.gz',
  keywords = ['dns', 'route53', 'aws', 'records'],
  install_requires=[
    'boto3>=1.4.4'
  ],
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ],
  long_description_content_type='text/markdown',
  long_description="""
  # route53_weighted_records
  Python package to manage over 100 weighted records under one url in AWS Route53.
  
  ## The Problem This Package Solves
  
  If you want to distribute requests to more than 100 endpoints behind a single
  url in Route53, you have to manage a tree-like structure of records since
  Route53 only supports up to 100 alternative responses for a single record.
  
  http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialManagingOver100WRR.html
  
  This library provides a simple create/delete interface for your url, and manages
  the tree structure behind the scenes.
  
  
  ## Usage
  
  ### Configure AWS Credentials
  First make sure boto has the correct access previleges to modify your Route53 records.
  The permssions can be configured through any of the means listed here:
  http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
  
  ### Code Examples
  
  ```
  from route53weightedrecords import Route53Manager
  
  # Create the manager (replace the hosted zone id and url with your own)
  manager = Route53Manager("my-hosted-zone-id", "my-cool-url.com.")
  
  # Create the record sets
  manager.create_record_sets(["192.168.1.1", "192.168.1.2", "192.168.1.3"])
  
  # The DNS entries should now show up in your Route53 console the proper weights!
  
  # Delete the record sets
  manager.delete_record_sets(["192.168.1.1", "192.168.1.2", "192.168.1.3"])
  ```
  
  ## Considerations
  
  This package assigns all responses the same weight so requests to the url will be
  equally balanced between the ips you add.  You cannot configure the weight of specific
  responses at this time.
  
  This package only supports up to 10,000 weigted records for a given url, not the full
  1,000,000 records that AWS allows.
  
  The Route53 has a rate limit of 5 requests per second, so make sure to adhere to that limit.
  
  ## Future Work
  
  * Support up to 1,000,000 responses for a single url.
  * Support weights when inserting reponses for a url.
  
  """
)
