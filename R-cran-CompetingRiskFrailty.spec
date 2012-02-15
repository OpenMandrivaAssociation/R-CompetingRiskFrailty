%define modulename CompetingRiskFrailty
%define realver 2.0
%define r_library %{_libdir}/R/library

Summary:	Competing risk model with frailties for right censored survival data for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 6
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The package offers a fitting of smooth varying coefficients in a 
competing risks modelling of hazards as well as estimating of the 
frailties (or unobserved heterogenities) for clustered observations.
Nonparametric penalized spline (p-spline) fitting of smooth covariates 
effects is proposed. As a spline basis truncated polynomial functions 
are chosen. The frailties are also fitted (via the EM-algoritghm) in a 
flexible way using a penalizied mixture of gamma distributions.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
