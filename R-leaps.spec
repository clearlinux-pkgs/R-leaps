#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-leaps
Version  : 3.1
Release  : 49
URL      : https://cran.r-project.org/src/contrib/leaps_3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/leaps_3.1.tar.gz
Summary  : Regression Subset Selection
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-leaps-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
This package performs an exhaustive search for the best subsets of a given
set of potential regressors, using a branch-and-bound algorithm, and also
performs searches using a number of less time-consuming techniques. It is
designed to replace the "leaps()" command in S.  It is based on FORTRAN77
code by Alan Miller of CSIRO Division of Mathematics & Statistics, which is
described in more detail in his book "Subset Selection in Regression".
Parts of the code have been published in the Applied Statistics algorithms series.

%package lib
Summary: lib components for the R-leaps package.
Group: Libraries

%description lib
lib components for the R-leaps package.


%prep
%setup -q -c -n leaps
cd %{_builddir}/leaps

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641045799

%install
export SOURCE_DATE_EPOCH=1641045799
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaps
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc leaps || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/leaps/DESCRIPTION
/usr/lib64/R/library/leaps/INDEX
/usr/lib64/R/library/leaps/Meta/Rd.rds
/usr/lib64/R/library/leaps/Meta/features.rds
/usr/lib64/R/library/leaps/Meta/hsearch.rds
/usr/lib64/R/library/leaps/Meta/links.rds
/usr/lib64/R/library/leaps/Meta/nsInfo.rds
/usr/lib64/R/library/leaps/Meta/package.rds
/usr/lib64/R/library/leaps/NAMESPACE
/usr/lib64/R/library/leaps/NEWS
/usr/lib64/R/library/leaps/R/leaps
/usr/lib64/R/library/leaps/R/leaps.rdb
/usr/lib64/R/library/leaps/R/leaps.rdx
/usr/lib64/R/library/leaps/help/AnIndex
/usr/lib64/R/library/leaps/help/aliases.rds
/usr/lib64/R/library/leaps/help/leaps.rdb
/usr/lib64/R/library/leaps/help/leaps.rdx
/usr/lib64/R/library/leaps/help/paths.rds
/usr/lib64/R/library/leaps/html/00Index.html
/usr/lib64/R/library/leaps/html/R.css
/usr/lib64/R/library/leaps/tests/nested.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/leaps/libs/leaps.so
/usr/lib64/R/library/leaps/libs/leaps.so.avx2
/usr/lib64/R/library/leaps/libs/leaps.so.avx512
