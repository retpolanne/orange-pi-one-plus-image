# Orange Pi One Plus Linux image

This is a repo for building your own Orange Pi One Plus image using Yocto.

## Installing hosttools

```sh
sudo pacman -Sy - < pacman.txt
yay -S - < yay.txt
```

## Baking image

```sh
source poky/oe-init-build-env orange-pi-one-plus
bitbake core-image-full-cmdline
```

## Pushing to SD Card

```sh

# Change /dev/sdX to your device
sudo bmaptool copy --bmap orange-pi-one-plus/tmp/deploy/images/orange-pi-one-plus/core-image-full-cmdline-orange-pi-one-plus.rootfs.wic.bmap orange-pi-one-plus/tmp/deploy/images/orange-pi-one-plus/core-image-full-cmdline-orange-pi-one-plus.rootfs.wic.gz /dev/sdX
```

## Testing

Install tbot - python-pipx is needed:

```sh
pipx install git+https://github.com/rahix/tbot@v0.10.5
```

Running a test

```sh
newbot -c config.orange_pi_test_config tc.interactive.test_uboot_dhcp
```
