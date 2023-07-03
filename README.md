# Orange Pi One Plus Linux image

This is a repo for building your own Orange Pi One Plus image using Yocto.

## Installing hosttools

```sh
sudo pacman -Sy - < pacman.txt
yay -S - < yay.txt
```

## Baking image

```sh
export MACHINE=orange-pi-one-plus
source poky/oe-init-build-env
bitbake core-image-minimal
```

## Pushing to SD Card

```sh

# Change /dev/sdX to your device
sudo bmaptool copy --bmap orange-pi-one-plus/tmp/deploy/images/orange-pi-one-plus/core-image-minimal-orange-pi-one-plus.rootfs.wic.bmap orange-pi-one-plus/tmp/deploy/images/orange-pi-one-plus/core-image-minimal-orange-pi-one-plus.rootfs.wic.gz /dev/sdX
```
