from distutils.core import setup

setup(
  name = 'route53weightedrecords',
  packages = ['route53weightedrecords'],
  version = '0.1',
  description = 'Python package to manage over 100 weighted records in AWS Route53.',
  author = 'Benjamin Liu',
  author_email = 'ben@mightysignal.com',
  url = 'https://github.com/benliu01/route53_weighted_records',
  download_url = 'https://github.com/benliu01/route53_weighted_records/archive/0.3.tar.gz',
  keywords = ['dns', 'route53', 'aws', 'records'],
  install_requires=[
    'boto3>=1.4.4'
  ],
  classifiers = []
)
