Summary:	Tool for .pot convert
Summary(pl):	Narzêdzie do konwersji plików .pot
Name:		i18ndude
Version:	0.5
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/plone-i18n/%{name}.tar.gz
# Source0-md5:	aec7a85b2c9b99180e89417f58ce96bc
URL:		http://sourceforge.net/projects/plone-i18n/
BuildRequires:	python
%pyrequires_eq	python-libs
Requires:	python-PyXML
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i18ndude is a tool for .pot convert.

%description -l pl
i18ndude jest narzêdziem do konwersji plików .pot.

%prep
%setup -q -c %{name}-%{ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
cp -af %{name}/i18ndude.py $RPM_BUILD_ROOT%{_bindir}
cp -af %{name}/{c*.py,*.pt,o*.py,r*.py,u*.py,v*.py} $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/{ChangeLog,README.txt,TODO.txt}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*.py*
%{py_sitescriptdir}/*.pt
