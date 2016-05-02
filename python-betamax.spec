%global srcname betamax
%global sum     A VCR imitation for python-requests

Name:           python-%{srcname}
Version:        0.7.0
Release:        1%{?dist}
Summary:        %{sum}

%{?python_provide:%python_provide python-%{srcname}}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/betamax
Source0:        https://pypi.python.org/packages/cc/bd/4879257f4d7c44bb3f19b9d48c9b5e5d1f4ea6efab2d4da48c6bd55468ff/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
BuildRequires:  python-requests
BuildRequires:  pytest
BuildRequires:  python-setuptools python3-setuptools

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests
much easier.


%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Betamax is a VCR_ imitation for requests. This will make mocking out requests
much easier.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python-%{srcname}
%doc PKG-INFO
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py2.*.egg-info

%files -n python3-%{srcname}
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.*.egg-info

%changelog
* Mon May 02 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.7.0-1
- Update to 0.7.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.5.1-1
- Initial packaging

