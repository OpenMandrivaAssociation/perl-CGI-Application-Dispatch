%define module   CGI-Application-Dispatch
%define version  2.13
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Dispatch requests to CGI::Application based object
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
BuildRequires: perl(CGI::Application)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::LongString)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides a way (as a mod_perl handler or running under vanilla CGI)
to look at the path ($r->path_info or $ENV{PATH_INFO}) of the incoming request,
parse off the desired module and it's run mode, create an instance of that
module and run it.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes TODO
%{_mandir}/man3/*
%perl_vendorlib/*


