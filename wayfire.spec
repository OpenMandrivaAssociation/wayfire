Name:           wayfire
Version:        0.7.4
Release:        1
Summary:        3D wayland compositor
Group:          WM/Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire
Source0:        https://github.com/WayfireWM/wayfire/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson
BuildRequires:  wf-touch
BuildRequires:  pkgconfig(wf-utils)
#BuildRequires:  cmake(doctest)
BuildRequires:  pkgconfig(glm)
 
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wf-config) >= 0.7.0
BuildRequires:  pkgconfig(wlroots) >= 0.15.0
BuildRequires:  pkgconfig(xkbcommon)

Requires: wf-utils

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.
 
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
Development files for %{name}.
 
 
%prep
%autosetup -p1

%build
%meson  \
        -Dxwayland=enabled \
        -Duse_system_wfconfig=enabled \
        -Duse_system_wlroots=enabled
%meson_build
 
%install
%meson_install
install -Dpm0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop


%files
%license LICENSE
%doc README.md %{name}.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{name}/

 
%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/
