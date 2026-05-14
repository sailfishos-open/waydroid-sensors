Name: waydroid-sensors
Version: 0.2.0
Release: 1
License: GPLv3
Summary: Waydroid sensors daemon

BuildRequires: cmake
BuildRequires: glib2-devel
BuildRequires: libgbinder-devel
BuildRequires: libglibutil-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)

Source0: %{name}-%{version}.tar.gz

%description
Sensors library for Waydroid


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make_build

%install
%make_install

%files
%{_bindir}/waydroid-sensord
