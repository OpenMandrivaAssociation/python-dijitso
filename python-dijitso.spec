%global	module dijitso
%global fname %(n=%{name}; echo ${n:0:1})

Summary:	An instant inlining of C and C++ code in Python
Name:		python-%{module}
Version:	2019.1.0
Release:	2
License:	LGPLv3+
Group:		Development/Python
URL:		https://fenicsproject.org
Source0:	https://bitbucket.org/fenics-project/%{module}/downloads/%{module}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/%{fname}/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(setuptools)

BuildRequires:	python3dist(mpi4py)
BuildRequires:  openmpi-devel

%description
A Python module for distributed just-in-time shared library building.

Instant is part of the FEniCS Project.

%files
%license COPYING
%license COPYING.LESSER
%doc README.rst
%{_bindir}/%{module}
%{py_sitedir}/%{module}/
%{py_sitedir}/fenics_%{module}-%{version}-py%{python_version}.egg-info/
%{_mandir}/man1/%{module}.1*

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

