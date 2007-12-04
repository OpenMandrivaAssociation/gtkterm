Name:           gtkterm
Version:        0.99.5
Release:        %mkrel 1

Summary:        Serial port terminal

Group:          Communications
License:        GPL
URL:            http://www.jls-info.com/julien/linux
Source0:        http://www.jls-info.com/julien/linux/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot 

BuildRequires:  gtk2-devel 
BuildRequires:  gettext 
BuildRequires:  bison 
BuildRequires:  vte-devel 
BuildRequires:  zlib-devel 
BuildRequires:  ncurses-devel

%description
Simple GUI terminal used to communicate with the serial port.
Similar to minicom or hyperterminal.

%prep
%setup -q


%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


# Menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
# FIXME : Add icons into menu
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%name): needs="x11" \
section="More Applications/Communications" \
title="Gtkterm" longtitle="%{summary}" command="%{name}"  
#icon="%{name}.png"
EOF
#


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_menudir}/%{name}
%{_mandir}/man1/%{name}.1*


