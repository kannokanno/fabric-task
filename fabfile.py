# -*- coding: utf-8 -*-
import re
from fabric.api import env, local, run, sudo

"""
host config
"""
def vagrant():
    env.user = 'vagrant'
    # port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']

    # vagrantのssh設定を使う
    # vagrant ssh-configを使うのでboxがあるディレクトリで実行する必要がある
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = re.search('"(.*)"', result).group(1)


"""
sample coomand
"""
def hello():
    run('uname -n')
    run('pwd')


"""
install commands
"""
def git():
    sudo('yum -y install git')
