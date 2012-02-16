%global packname  CompetingRiskFrailty
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          2.0
Release:          1
Summary:          Competing Risk Model with Frailties for Right Censored Survival Data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-CompetingRiskFrailty

%description
The package offers a fitting of smooth varying coefficients in a competing
risks modelling of hazards as well as estimating of the frailties (or
unobserved heterogenities) for clustered observations. Nonparametric
penalized spline (p-spline) fitting of smooth covariates effects is
proposed. As a spline basis truncated polynomial functions are chosen. The
frailties are also fitted (via the EM-algoritghm) in a flexible way using
a penalizied mixture of gamma distributions.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
