Name:           perl-IPC-LockTicket
Version:        2.1
Release:        1%{?dist}
Summary:        IPC::LockTicket - Interprocess communication via Storable library

License:        GPLv3
URL:            https://github.com/DomAsProgrammer/perl-IPC-LockTicket
Source0:        IPC-LockTicket-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  perl >= 5.32.1
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(CPAN)

Requires:  perl(Storable)
Requires:  perl(Try)
Requires:  perl(boolean)
Requires:  perl(List::Util)
Requires:  perl(utf8)
Requires:  perl(Time::HiRes)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
IPC::LockTicket is a OO library to share (IPC) locks/token via the Storeable library. It also has an interface to transfer data, but this might decrease the speed of your application using this feature.


%prep
%autosetup -n IPC-LockTicket-%{version}


%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
# For noarch packages: vendorlib
%{perl_vendorlib}/*
#%exclude %dir %{perl_vendorarch}/auto/
#%{_mandir}/man3/*.3*


%changelog
* Tue Nov 07 2023 Dominik Bernhardt <domasprogrammer@gmail.com> - 1.2.5
- First init.
