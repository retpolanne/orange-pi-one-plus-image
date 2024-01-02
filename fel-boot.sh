#!/bin/bash

cd orange-pi-one-plus/tmp/deploy/images/orange-pi-one-plus

sudo ~/Dev/sunxi-tools/sunxi-fel -v uboot u-boot-sunxi-with-spl.bin \
        write 0x40200000 Image \
        write 0x4fa00000 sun50i-h6-orangepi-one-plus.dtbaaa \
        write 0x4fc00000 boot.scr \
        write 0x4ff00000 core-image-minimal-orange-pi-one-plus.rootfs.tar.gz

