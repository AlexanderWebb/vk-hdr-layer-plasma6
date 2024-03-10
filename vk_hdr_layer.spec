Name:           VK_hdr_layer
Version:        main
Release:        %autorelease
Summary:     Vulkan layer for HDR on Plasma 6.0

License:        MIT
URL:            https://github.com/Zamundaaa/VK_hdr_layer
Source:         https://github.com/Zamundaaa/VK_hdr_layer/archive/refs/heads/main.tar.gz

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(vkroots)

%description
Simple package of Zamundaa's VK_hdr_layer, used for experimental HDR on Plasma 6.

See https://zamundaaa.github.io/wayland/2023/12/18/update-on-hdr-and-colormanagement-in-plasma.html for other instructions.

I'm running this on Fedora Kinoite 40, so good luck on anything else.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/*
%{_libdir}/*.so
