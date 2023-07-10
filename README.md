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

```sh
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

Running a test

```sh
pytest -x -vs --tbot-config config.orange_pi_test_config tc/interactive.py
```
