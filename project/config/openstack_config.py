import os
from openstack import connection
from dotenv import load_dotenv

load_dotenv()

openstack_auth = {
    'auth_url': os.environ['OS_AUTH_URL'],
    'project_name': os.environ['OS_PROJECT_NAME'],
    'username': os.environ['OS_USERNAME'],
    'password': os.environ['OS_PASSWORD'],
    'user_domain_name': os.environ.get('OS_USER_DOMAIN_NAME', None),
    'project_domain_id': os.environ.get('OS_PROJECT_DOMAIN_ID', None),
    'region_name': os.environ.get('OS_REGION_NAME', None),
    'interface': os.environ.get('OS_INTERFACE', 'public'),
    'identity_api_version': os.environ.get('OS_IDENTITY_API_VERSION', '3'),
}

conn = connection.Connection(**openstack_auth)

