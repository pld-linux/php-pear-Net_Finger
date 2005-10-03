%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Finger
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - querying finger servers
Summary(pl):	%{_pearname} - odpytywanie serwer�w fingera
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	cffe5878aa31a24b04963bbd7fe3db02
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Net_Finger/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_Socket
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Finger class provides a tool for querying Finger
Servers.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Net_Finger dostarcza narz�dzi do odpytywania serwer�w
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
