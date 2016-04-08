from fabric import api as fab
from fabric.context_managers import cd

def make_virtualbox():
    fab.local('packer build -only=virtualbox-iso ./example.json')

def make_ami():
    fab.local('packer build -only=amazon-ebs ./example.json')

def regen_keys():
    """
    Regenerate the ssh keys used by packer, and the created Virtualbox .box file

    You should run this after cloning the repo, so you're not using the *base*
    keys.  (Those are checked in publicly.)

    ** be aware **
    - This *removes* the keys permanently!  You can't get them back.  Make sure
    this is what you want to do before running this fab command!

    This only affects the LOCAL packer build.  Amazon uses its own ssh config,
    so you won't have to worry about this affecting an Amazon build.
    """
    fab.local('rm files/vagrant')
    fab.local('rm files/vagrant.pub')
    fab.local('ssh-keygen -b 4096 -t rsa -f files/vagrant -q -N ""')
