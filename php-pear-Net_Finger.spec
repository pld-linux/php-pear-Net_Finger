%define		_class		Net
%define		_subclass	Finger
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - querying finger servers
Summary(pl.UTF-8):	%{_pearname} - odpytywanie serwerów fingera
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a6c1783516dca3c450ee19fbeb29bb4d
URL:		http://pear.php.net/package/Net_Finger/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Finger class provides a tool for querying Finger
Servers.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::Net_Finger dostarcza narzędzi do odpytywania serwerów
fingera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
