%include	/usr/lib/rpm/macros.python
Summary:	Tool for .pot convert
Summary(pl):	Narz�dzie do konwersji plik�w .pot
Name:		i18ndude
Version:	0.2.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/plone-i18n/%{name}.tar.gz
# Source0-md5:	aec7a85b2c9b99180e89417f58ce96bc
URL:		http://sourceforge.net/projects/plone-i18n/
Requires:	python-PyXML
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i18ndude is a tool for .pot convert.

%description -l pl
i18ndude jest narz�dziem do konwersji plik�w .pot.

%prep
%setup -q -c %{name}-%{ver}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sbindir}
cp -af %{name}/{*.py,*.pt} $RPM_BUILD_ROOT/%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/{README.txt,TODO.txt}
%attr(755,root,root) %{_sbindir}/*
