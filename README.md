# VK_hdr_layer RPM spec

RPM Spec file to install https://github.com/Zamundaaa/VK_hdr_layer

## Why

That vulkan layer is necessary to use HDR on plasma 6. Making an RPM and associated COPR makes it easier to install/update on my desktop running Fedora Kinoite.

COPR available at https://copr.fedorainfracloud.org/coprs/atwebb/vk_hdr_layer_plasma6

## Build

Dependencies:
- `dnf group install "rpm development tools"`

```bash
spectool -g vk_hdr_layer.spec
fedpkg --release f40 mockbuild
```

or any future fedora version like `f41`, but this vulkan layer should get merged to Mesa drivers pretty quick. I saw a forum post saying ETA end of 2024.
