#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install freetds freetds-devel tree vim
wget https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm
sudo rpm -ivh pgdg-centos95-9.5-2.noarch.rpm
sudo yum install postgresql95 postgresql95-server postgresql95-libs postgresql95-devel

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
	SCRIPTPATH=/vagrant
fi

mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES

wget https://github.com/tds-fdw/tds_fdw/archive/v1.0.7.tar.gz
