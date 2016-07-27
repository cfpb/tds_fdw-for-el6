# tds_fdw-1.0.7 RPM built for RHEL 6.X

**Description**:  

    A TDS foreign data wrapper. It can be used to connect to Microsoft SQL Server and Sybase databases.

## Dependencies

    None 

## Installation

    Requires a library that implements the DB-Library interface, such as FreeTDS 
    (download epel repository and install freetds and freetds-devel)

    Also, to install PostgreSQL (if not installed already)
    you can visit https://wiki.postgresql.org/wiki/YUM_Installation 

    OR 

    wget https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm
    sudo rpm -ivh pgdg-centos95-9.5-2.noarch.rpm
    sudo yum install postgresql95 postgresql95-server postgresql95-libs postgresql95-devel

### Build the RPM using Vagrant

1. Once the repo has been cloned, run "vagrant up" to create the build VM
2. Run "vagrant ssh" to connect
3. CD to ~/rpmbuild
4. Run "rpmbuild -ba SPECS/fdw_tds.spec"

### Build the RPM on a server
1. Once the repo has been cloned, run "sh ./bootstrap.sh"
2. CD to ~/rpmbuild
3. Run "rpmbuild -ba SPECS/fdw_tds.spec"

### Install the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/.rpm"

## Configuration

Edit the SPEC file to make changes to the build configuration.


## Known issues

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

To contribute, please see [CONTRIBUTING](CONTRIBUTING.md).

----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

----
