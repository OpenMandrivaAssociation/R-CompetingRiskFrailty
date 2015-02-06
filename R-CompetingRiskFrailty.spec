%global packname  CompetingRiskFrailty
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          2.0
Release:          3
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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:2.0-1
+ Revision: 774959
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:1.0-1
+ Revision: 774625
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-6mdv2011.0
+ Revision: 616440
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2010.0
+ Revision: 433078
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.0-4mdv2009.0
+ Revision: 260127
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.0-3mdv2009.0
+ Revision: 248229
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0-1mdv2008.1
+ Revision: 169920
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-CompetingRiskFrailty.

