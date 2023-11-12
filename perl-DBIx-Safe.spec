Name:           perl-DBIx-Safe
Version:        1.2.5
Release:        1%{?dist}
Summary:        DBIx::Safe - Safer access to your database through a DBI database handle

License:        BSD
URL:            https://metacpan.org/pod/DBIx::Safe
Source0:        https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBIx-Safe-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Harness)

Requires:  perl(DBD::Pg)
Requires:  perl(DBI)
Requires:  perl(Test::Simple)
Requires:  perl(Test::More)
Requires:  perl(Test::Harness)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The purpose of this module is to give controlled, limited access to an application, rather than simply passing it a raw database handle through DBI. DBIx::Safe acts as a wrapper to the database, by only allowing through the commands you tell it to. It filters all things related to the database handle - methods and attributes.

The typical usage is for your application to create a database handle via a normal DBI call to new(), then pass that to DBIx::Safe->new(), which will return you a DBIx::Safe object. After specifying exactly what is and what is not allowed, you can pass the object to the untrusted application. The object will act very similar to a DBI database handle, and in most cases can be used interchangeably.

By default, nothing is allowed to run at all. There are many things you can control. You can specify which SQL commands are allowed, by indicating the first word in the SQL statement (e.g. 'SELECT'). You can specify which database methods are allowed to run (e.g. 'ping'). You can specify a regular expression that allows matching SQL statements to run (e.g. 'qr{SET TIMEZONE}'). You can specify a regular expression that is NOT allowed to run (e.g. qr(UPDATE xxx}). Finally, you can indicate which database attributes are allowed to be read and changed (e.g. 'PrintError'). For all of the above, there are matching methods to remove them as well.


%prep
%autosetup -n DBIx-Safe-%{version}


%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
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
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
* Tue Nov 07 2023 Dominik Bernhardt <domasprogrammer@gmail.com> - 1.2.5
- Basic Perl type package
