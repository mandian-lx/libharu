%define ver %(echo %version | tr \. \_ )

%define major	2.3.0
%define libname %mklibname haru %{major}
%define devname %mklibname haru -d

Summary:	A free, cross platform, open source library for generating PDF file
Name:		libharu
Version:	2.3.0
Release:	0
License:	zlib with acknowledgement
Group:		System/Libraries
URL:		http://libharu.org
Source0:	https://github.com/%{name}/%{name}/archive/RELEASE_%{ver}.tar.gz

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
Haru is a free, cross platform, open-sourced software library for generating
PDF.

It supports the following features:

  · Generating PDF files with lines, text, images.
  · Outline, text annotation, link annotation.
  · Compressing document with deflate-decode.
  · Embedding PNG, Jpeg images.
  · Embedding Type1 font and TrueType font.
  · Creating encrypted PDF files.
  · Using various character sets (ISO8859-1~16, MSCP1250~8, KOI8-R).
  · Supporting CJK fonts and encodings.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A free, cross platform, open source library for generating PDF file
Group:		System/Libraries

%description -n %{libname}
Haru is a free, cross platform, open-sourced software library for generating
PDF.

It supports the following features:

  · Generating PDF files with lines, text, images.
  · Outline, text annotation, link annotation.
  · Compressing document with deflate-decode.
  · Embedding PNG, Jpeg images.
  · Embedding Type1 font and TrueType font.
  · Creating encrypted PDF files.
  · Using various character sets (ISO8859-1~16, MSCP1250~8, KOI8-R).
  · Supporting CJK fonts and encodings.

%files -n %{libname}
%{_libdir}/libhpdf-%{version}.so*
%doc README

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	 A free, cross platform, open source library for generating PDF file
Group:		 Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Headers and development files for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libhpdf.so
%doc CHANGES

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-RELEASE_%{ver}

%build
autoreconf -fiv
%configure --enable-debug --disable-static
%make

%install
%makeinstall_std

