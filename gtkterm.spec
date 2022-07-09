Summary:	Serial port terminal
Name:		gtkterm
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Communications
URL:		https://github.com/Jeija/gtkterm
Source0:        https://github.com/Jeija/gtkterm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(gudev-1.0)

%description
Gtkterm is a simple GTK+ terminal used to communicate with a serial port.
It is has fewer features than minicom, but is designed to be as easy to
use as possible.

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
