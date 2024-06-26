#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lhs
Version  : 1.1.6
Release  : 51
URL      : https://cran.r-project.org/src/contrib/lhs_1.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lhs_1.1.6.tar.gz
Summary  : Latin Hypercube Samples
Group    : Development/Tools
License  : GPL-3.0
Requires: R-lhs-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-lhs package.
Group: Libraries

%description lib
lib components for the R-lhs package.


%prep
%setup -q -n lhs
cd %{_builddir}/lhs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671480790

%install
export SOURCE_DATE_EPOCH=1671480790
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lhs/DESCRIPTION
/usr/lib64/R/library/lhs/INDEX
/usr/lib64/R/library/lhs/Meta/Rd.rds
/usr/lib64/R/library/lhs/Meta/features.rds
/usr/lib64/R/library/lhs/Meta/hsearch.rds
/usr/lib64/R/library/lhs/Meta/links.rds
/usr/lib64/R/library/lhs/Meta/nsInfo.rds
/usr/lib64/R/library/lhs/Meta/package.rds
/usr/lib64/R/library/lhs/Meta/vignette.rds
/usr/lib64/R/library/lhs/NAMESPACE
/usr/lib64/R/library/lhs/NEWS
/usr/lib64/R/library/lhs/R/lhs
/usr/lib64/R/library/lhs/R/lhs.rdb
/usr/lib64/R/library/lhs/R/lhs.rdx
/usr/lib64/R/library/lhs/doc/augment_lhs.R
/usr/lib64/R/library/lhs/doc/augment_lhs.Rmd
/usr/lib64/R/library/lhs/doc/augment_lhs.html
/usr/lib64/R/library/lhs/doc/index.html
/usr/lib64/R/library/lhs/doc/lhs_basics.R
/usr/lib64/R/library/lhs/doc/lhs_basics.Rmd
/usr/lib64/R/library/lhs/doc/lhs_basics.html
/usr/lib64/R/library/lhs/doc/lhs_faq.R
/usr/lib64/R/library/lhs/doc/lhs_faq.Rmd
/usr/lib64/R/library/lhs/doc/lhs_faq.html
/usr/lib64/R/library/lhs/help/AnIndex
/usr/lib64/R/library/lhs/help/aliases.rds
/usr/lib64/R/library/lhs/help/lhs.rdb
/usr/lib64/R/library/lhs/help/lhs.rdx
/usr/lib64/R/library/lhs/help/paths.rds
/usr/lib64/R/library/lhs/html/00Index.html
/usr/lib64/R/library/lhs/html/R.css
/usr/lib64/R/library/lhs/tests/testthat.R
/usr/lib64/R/library/lhs/tests/testthat/helper-lhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-augmentlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-create_oalhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-createoa.R
/usr/lib64/R/library/lhs/tests/testthat/test-galois_field.R
/usr/lib64/R/library/lhs/tests/testthat/test-geneticlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-get_library_versions.R
/usr/lib64/R/library/lhs/tests/testthat/test-improvedlhs.r
/usr/lib64/R/library/lhs/tests/testthat/test-maximinlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-oa_to_oalhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-optaugmentlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-optimumlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-optseededlhs.R
/usr/lib64/R/library/lhs/tests/testthat/test-randomlhs.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lhs/libs/lhs.so
/usr/lib64/R/library/lhs/libs/lhs.so.avx2
/usr/lib64/R/library/lhs/libs/lhs.so.avx512
