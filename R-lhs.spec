#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lhs
Version  : 0.16
Release  : 4
URL      : https://cran.r-project.org/src/contrib/lhs_0.16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lhs_0.16.tar.gz
Summary  : Latin Hypercube Samples
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lhs-lib
Requires: R-RUnit
BuildRequires : R-RUnit
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-lhs package.
Group: Libraries

%description lib
lib components for the R-lhs package.


%prep
%setup -q -c -n lhs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530340589

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530340589
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lhs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lhs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lhs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lhs|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/lhs/R/lhs
/usr/lib64/R/library/lhs/R/lhs.rdb
/usr/lib64/R/library/lhs/R/lhs.rdx
/usr/lib64/R/library/lhs/doc/augmentLHS_Example.R
/usr/lib64/R/library/lhs/doc/augmentLHS_Example.Rtex
/usr/lib64/R/library/lhs/doc/augmentLHS_Example.pdf
/usr/lib64/R/library/lhs/doc/index.html
/usr/lib64/R/library/lhs/help/AnIndex
/usr/lib64/R/library/lhs/help/aliases.rds
/usr/lib64/R/library/lhs/help/lhs.rdb
/usr/lib64/R/library/lhs/help/lhs.rdx
/usr/lib64/R/library/lhs/help/paths.rds
/usr/lib64/R/library/lhs/html/00Index.html
/usr/lib64/R/library/lhs/html/R.css
/usr/lib64/R/library/lhs/libs/symbols.rds
/usr/lib64/R/library/lhs/unitTests/runit_augmentLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_geneticLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_improvedLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_maximinLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_optAugmentLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_optSeededLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_optimumLHS.r
/usr/lib64/R/library/lhs/unitTests/runit_randomLHS.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lhs/libs/lhs.so
/usr/lib64/R/library/lhs/libs/lhs.so.avx2
/usr/lib64/R/library/lhs/libs/lhs.so.avx512
