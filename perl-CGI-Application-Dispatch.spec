%define upstream_name    CGI-Application-Dispatch
%define upstream_version 2.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Dispatch requests to CGI::Application based object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Exception::Class::TryCatch)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a way (as a mod_perl handler or running under vanilla CGI)
to look at the path ($r->path_info or $ENV{PATH_INFO}) of the incoming request,
parse off the desired module and it's run mode, create an instance of that
module and run it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
