%define _disable_ld_no_undefined 1

Name:           wayfire
Version:        0.10.0
Release:        2
Summary:        3D wayland compositor
Group:          WM/Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire
Source0:        https://github.com/WayfireWM/wayfire/releases/download/v%{version}/%{name}-%{version}.tar.xz
 
BuildRequires:  cmake
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson
#BuildRequires:  wf-touch
#BuildRequires:  pkgconfig(wf-utils)
BuildRequires:  cmake(doctest)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  gomp-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wf-config) >= 0.8.0
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(yyjson)

Recommends: wcm
Recommends: wf-shell
Recommends: xdg-desktop-portal-wlr
Recommends: wayfire-plugins-extra
Recommends: wf-osk

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
# As of wayfire 0.8.1 and LLVM 18.1 compiler crashing. Switch to GGC for now.
# With wayfire 0.10 back again to GCC because wayfire with Clang crashing at runtime.
# Dont switch back to Clang without re testing!
export CC=gcc
export CXX=g++
%meson  \
        -Dxwayland=enabled \
        -Duse_system_wfconfig=enabled \
        -Duse_system_wlroots=enabled \
        -Dtests=disabled
%meson_build
 
%install
%meson_install
install -Dpm0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
rm -f %{buildroot}%{_libdir}/libwftouch.a

%files
%license LICENSE
%doc README.md %{name}.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/*.desktop
%{_datadir}/xdg-desktop-portal/wayfire-portals.conf
%{_libdir}/%{name}/
%{_libdir}/libwf-utils.so.0*
%{_libdir}/libwayfire-blur-base.so
%{_libdir}/libwayfire-move-drag-interface.a
%{_libdir}/libwayfire-workspace-wall.a
%{_mandir}/man1/wayfire.1.*

%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/
