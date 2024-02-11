#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Context library
Summary(pl.UTF-8):	Biblioteka Oslo Context
Name:		python-oslo.context
# keep 2.x here for python2 support
Version:	2.23.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/oslo.context/
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.context/oslo.context-%{version}.tar.gz
# Source0-md5:	e34051c37ed531003375fa1535b53fd1
URL:		https://pypi.org/project/oslo.context/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-debtcollector >= 1.2.0
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-stestr >= 2.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-debtcollector >= 1.2.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-stestr >= 2.0.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

%description -l pl.UTF-8
Biblioteka Oslo context zawiera funkcje pomocnicze do utrzymywania
przydatnych informacji o kontekście żądania. Kontest ten jest zwykle
wypełniany w potoku WSGI i używany przez różne moduły, np. logowanie.

%package -n python3-oslo.context
Summary:	Oslo Context library
Summary(pl.UTF-8):	Biblioteka Oslo Context
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-oslo.context
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

%description -n python3-oslo.context -l pl.UTF-8
Biblioteka Oslo context zawiera funkcje pomocnicze do utrzymywania
przydatnych informacji o kontekście żądania. Kontest ten jest zwykle
wypełniany w potoku WSGI i używany przez różne moduły, np. logowanie.

%package apidocs
Summary:	API documentation for Python oslo.context module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.context
Group:		Documentation

%description apidocs
API documentation for Python oslo.context module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.context.

%prep
%setup -q -n oslo.context-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_context
%{py_sitescriptdir}/oslo.context-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.context
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_context
%{py3_sitescriptdir}/oslo.context-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
