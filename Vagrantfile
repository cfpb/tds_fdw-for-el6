# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :tds do |tds_config|
    tds_config.vm.box = "bento/centos-6.7"
    tds_config.vm.hostname = "tds"
    tds_config.vm.network :private_network, ip: "192.168.1.22"
    tds_config.vm.provider "virtualbox" do |vb|
    end
    tds_config.vm.provision :shell, path: "bootstrap.sh", privileged: false
  end

end
