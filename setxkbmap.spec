Name:		setxkbmap
Version:	1.3.1
Release:	2
Summary:	Set the keyboard using the X Keyboard Extension
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The setxkbmap command maps the keyboard to use the layout determined by the
options specified on the command line.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1.*
