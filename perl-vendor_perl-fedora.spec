Name:       perl-vendor_perl-fedora
Version:    1
Release:    2.sl6
License:    GPLv2+
Summary:    Fixes issue with 'perl -V:installvendorlib' and 'perl -V:installvendorarch'
Group:      Applications/System
URL:        http://www.scientificlinux.org
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:  noarch

%description
Fixes issue with 'perl -V:installvendorlib' and 'perl -V:installvendorarch'

%files

%triggerin -- perl
for file in /usr/lib/perl5/Config_heavy.pl /usr/lib64/perl5/Config_heavy.pl
do
  if [ -s $file ] ; then
      sed -i.save -e 's|\/vendor_perl||g' $file
  fi
done

%changelog
* Thu Dec 09 2010 Connie Sieh <csieh@fnal.gov> 1.sl 
- SL 6 first release 
