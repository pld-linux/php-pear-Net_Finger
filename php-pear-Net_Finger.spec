%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Finger
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - querying finger servers
Summary(pl):	%{_pearname} - odpytywanie serwerów fingera
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	cffe5878aa31a24b04963bbd7fe3db02
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Net_Finger/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Finger class provides a tool for querying Finger
Servers.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa PEAR::Net_Finger dostarcza narzêdzi do odpytywania serwerów
fingera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
