###########################
%global debug_package %{nil}

Name:           tds_fdw
Version:        1.0.7
Release:        1%{?dist}
Summary:        TDS foreing data wrapper for PostgreSQL 9.4

Group:          Development/Tools
License:        None
URL:            https://github.com/GeoffMontee/tds_fdw
Source:         https://github.com/tds-fdw/tds_fdw/archive/v1.0.7.tar.gz

Requires:       postgresql95 >= 9.4.1
Requires:       postgresql95-server >= 9.4.1
Requires:       postgresql95-libs >= 9.4.1
Requires:       freetds >= 0.91

BuildRequires:  freetds-devel, postgresql95-devel 
BuildRequires:  automake, gcc-c++

###########################
%description
This is a PostgreSQL foreign     data wrapper that can connect to databases that
use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.

###########################
%prep
%setup -q -n tds_fdw-1.0.7


###########################
%build
PATH=/usr/pgsql-9.5/bin:$PATH make USE_PGXS=1

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.5/bin:$PATH 
make USE_PGXS=1 install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}

###########################
%files
/usr/pgsql-9.5
