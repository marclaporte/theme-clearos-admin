Name: theme-clearos-admin
Group: Applications/Themes
Version: 7.0.12
Release: 1%{dist}
Summary: ClearOS 7 base theme
License: ClearCenter license
Packager: ClearCenter
Vendor: ClearCenter
Source: %{name}-%{version}.tar.gz
Requires: clearos-framework >= 7.0.12
Buildarch: noarch

%description
ClearOS Admin Theme

%prep
%setup -q
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/themes/ClearOS-Admin
cp -r * $RPM_BUILD_ROOT/usr/clearos/themes/ClearOS-Admin

%files
%defattr(-,root,root)
%dir /usr/clearos/themes/ClearOS-Admin
/usr/clearos/themes/ClearOS-Admin
