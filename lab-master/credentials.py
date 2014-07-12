import os


def get_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_credentials_tenant_one(username, password, tenant_name):
    d = {}
    d['username'] = username
    d['password'] = password
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = tenant_name
    return d

def get_cinder_credentials():
    d = [os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
         os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL']]
    return d


def get_credentials_tenant(tenant_name):
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = tenant_name
    return d


def get_nova_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_credentials_tenant(username, password, tenant_name, version):
    d = {}
    d['version'] = version 
    d['username'] = username
    d['api_key'] = password
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = tenant_name
    return d

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_credentials_v3():
    d = {}
    d['version'] = '3'
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    return d

def get_nova_credentials_v11():
    d = {}
    d['version'] = '1.1'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def get_ceilo_credentials():
    d = {}
    d['os_username'] = os.environ['OS_USERNAME']
    d['os_password'] = os.environ['OS_PASSWORD']
    d['os_auth_url'] = os.environ['OS_AUTH_URL']
    d['os_tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
