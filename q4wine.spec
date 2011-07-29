#
# spec file for package q4wine (Version 0.121)
#
# Copyright (c) 2009, 2010 Kyrill Detinov
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:		q4wine
Version:	0.121
Release:	1
License:	GPL v3
URL:		http://q4wine.brezblock.org.ua/
Source0:	http://downloads.sourceforge.net/project/q4wine/q4wine/q4wine%200.121/%{name}-%{version}.tar.bz2
# Source0-md5:	2de5de62f57ba6b26247198df339d81a
######		Unknown group!
Summary:	Qt4 GUI for WINE
Summary(pl.UTF-8):	Graficzna nakładka Qt4 dla WINE
Group:		Application/Emulators
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	cmake
BuildRequires:	fdupes
BuildRequires:	fuse-iso
BuildRequires:	icoutils
Requires:	fuse-iso
Requires:	icoutils
Requires:	sqlite3
Requires:	sudo
Requires:	wine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Q4Wine is an Qt4-based GUI for WINE. It will help you to manage wine
prefixes and installed applications.

General features:
- Can export Qt color theme into wine colors settings.
- Can easy work with different wine versions at the same time.
- Easy creating, deleting and managing prefixes (WINEPREFIX).
- Easy controlling for wine process.
- Autostart icons support.
- Easy cd-image use.
- You can extract icons from PE files (.exe .dll).
- Easy backup and restore for managed prefixes.
- Wine AppDB browser.
- Logging subsystem.
- Winetricks support.

%description -l pld.UTF-8
Q4Wine jest bazowaną na Qt4 graficzną nakładką WINE. Ułatwi Ci
zarządzanie prefiksami oraz zainstalowanymi aplikacjami..

Możliwości:
- Potrafi wyeksportować motyw kolorów Qt do ustawień kolorów wine.
- Ułatwi Ci pracę z wieloma wersjami wine naraz.
- Łatwe tworzenie, usuwanie i zarządzanie prefiksami (WINEPREFIX).
- Łatwa zarzadzanie procesami wine.
- Wsparcie dla ikon autostartu.
- Proste korzystanie z obrazów þlyt CD..
- Umożliwia wyciąganie ikon z plików PE (.exe .dll).
- Proste tworzenie kopii zapasowych prefiksów i ich przywracanie..
- Przeglądarka wine AppDB (bazy danych aplikacji).
- Podsystem logowania..
- Wsparcie dla Winetricks.

%prep
%setup -q

%build
%{__mkdir} build
cd build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DWITH_WINETRIKS=ON
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT
fdupes -s $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
