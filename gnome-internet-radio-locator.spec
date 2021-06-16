Name:           gnome-internet-radio-locator
Version:        10.0.1
Release:        1
Summary:        Live Internet radio broadcaster discovery program
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://wiki.gnome.org/Apps/InternetRadioLocator
Source0:        https://download.gnome.org/sources/%{name}/4.0/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.10
BuildRequires:	pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.12.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(pangoft2) >= 0.28
Provides:       girl

%description
GNOME Internet Radio Locator is a program that allows locating free
Internet radio stations by broadcasters with the help of a map.
It is developed with GNOME Maps, libchamplain and geocode-lib.

You can view all the stations in src/gnome-internet-radio-locator.xml
and enter city names in the GUI search input field in order to locate
radio stations in the city using the text search with auto-completion.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--with-recording \
	%{nil}
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
%find_lang %{name} %{?no_lang_C} %{name}.lang

%files
%license COPYING
%doc AUTHORS ChangeLog README THANKS NEWS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/gnome-internet-radio-locator/gnome-internet-radio-locator-5.0.dtd
%{_datadir}/%{name}/gnome-internet-radio-locator.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome-internet-radio-locator/doc/AAMOT.txt.xz
%{_datadir}/gnome-internet-radio-locator/doc/Aamot-2020.txt.xz
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.xml
%{_datadir}/locale/*/LC_MESSAGES/gnome-internet-radio-locator.mo
%{_mandir}/man1/gnome-internet-radio-locator.1.*
