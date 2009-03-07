Name: setxkbmap
Version: 1.0.4
Release: %mkrel 5
Summary: Set the keyboard using the X Keyboard Extension
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The setxkbmap command maps the keyboard to use the layout determined by the
options specified on the command line.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1.*
