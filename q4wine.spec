#
# spec file for package q4wine (Version 0.121)
#
# Copyright (c) 2009, 2010 Kyrill Detinov
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Summary:	Qt GUI for WINE
Summary(pl.UTF-8):	Graficzna nakładka Qt dla WINE
Name:		q4wine
Version:	1.4.2
Release:	1
License:	GPL v3
Source0:	https://github.com/brezerk/q4wine/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c98dbae975d6937f63845be119039801
Patch0:		libdir.patch
URL:		http://q4wine.brezblock.org.ua/
######		Unknown group!
Group:		Application/Emulators
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake
BuildRequires:	fdupes
BuildRequires:	fuse-iso
BuildRequires:	icoutils
BuildRequires:	qt6-linguist
Requires:	fuse-iso
Requires:	icoutils
Requires:	sqlite3
Requires:	sudo
Requires:	wine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Q4Wine is an Qt-based GUI for WINE. It will help you to manage wine
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
Q4Wine jest bazowaną na Qt graficzną nakładką WINE. Ułatwi Ci
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
%patch -P0 -p1

%build
mkdir -p build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

fdupes -s $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md Changelog.md README.md
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/q4wine*
%{_libdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/q4wine*.svg
%{_datadir}/metainfo/ua.org.brezblock.q4wine.appdata.xml
%{_mandir}/man1/q4wine*.1*
