Name:           libsass
Version:        3.3.6
Release:        1%{?dist}
Summary:        C/C++ port of the Sass CSS precompiler

License:        MIT
URL:            http://sass-lang.com/libsass
Source0:        https://github.com/sass/libsass/archive/%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig


%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original version was
written in Ruby, but this version is meant for efficiency and portability.

This library strives to be light, simple, and easy to build and integrate with
a variety of platforms and languages.

Libsass is just a library, but if you want to RUN libsass, install the sassc
package.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
autoreconf --force --install


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc Readme.md SECURITY.md
%{_libdir}/*.so.*

%files devel
%license LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Sep 30 2015 Aurelien Bompard <abompard@fedoraproject.org> - 3.3.6-1
- initial package
