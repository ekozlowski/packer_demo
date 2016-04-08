# -*- mode: ruby -*-
# vi: set ft=ruby :

boxes = [
  {
    :name => "packertest",
    :eth1 => "192.168.50.11",
    :mem => "1024",
    :cpu => "1",
    :hostport => "8065"
  }
]

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  boxes.each do |opts|
    config.vm.define opts[:name] do |config|
      config.ssh.private_key_path = './files/vagrant'
      config.vm.hostname = opts[:name]
      config.vm.box = "packerdemobox"
      config.vm.box_url = "./packdemo.box"
      config.vm.network "private_network", ip: opts[:eth1]
      config.vm.network "forwarded_port", guest: 80, host: opts[:hostport]
      config.vm.provider "virtualbox" do |v|
        v.memory = opts[:mem]
        v.cpus = opts[:cpu]
      end
    end
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "./test_playbook.yml"
    ansible.groups = {
      "packerdemo" => ["packertest"]
    }
  #  puppet.manifests_path = "../Puppet/manifests"
  #  puppet.manifest_file  = "nodes/palpatine.cmgeneral.local.pp"
  #  puppet.module_path = "../Puppet/modules"
  #end
  end
end
