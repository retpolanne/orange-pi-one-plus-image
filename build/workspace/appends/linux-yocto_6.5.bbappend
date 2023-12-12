FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"
FILESPATH:prepend := "/home/retpolanne/Dev/orange-pi-one-plus-image/build/workspace/sources/linux-yocto/oe-local-files:"
# srctreebase: /home/retpolanne/Dev/orange-pi-one-plus-image/build/workspace/sources/linux-yocto

inherit externalsrc
# NOTE: We use pn- overrides here to avoid affecting multiple variants in the case where the recipe uses BBCLASSEXTEND
EXTERNALSRC:pn-linux-yocto = "/home/retpolanne/Dev/orange-pi-one-plus-image/build/workspace/sources/linux-yocto"
SRCTREECOVEREDTASKS = "do_validate_branches do_kernel_checkout do_fetch do_unpack do_kernel_configcheck"

do_patch[noexec] = "1"

do_configure:append() {
    cp ${B}/.config ${S}/.config.baseline
    ln -sfT ${B}/.config ${S}/.config.new
}

do_kernel_configme:prepend() {
    if [ -e ${S}/.config ]; then
        mv ${S}/.config ${S}/.config.old
    fi
}

do_configure:append() {
    if [ ${@ oe.types.boolean('${KCONFIG_CONFIG_ENABLE_MENUCONFIG}') } = True ]; then
        cp ${KCONFIG_CONFIG_ROOTDIR}/.config ${S}/.config.baseline
        ln -sfT ${KCONFIG_CONFIG_ROOTDIR}/.config ${S}/.config.new
    fi
}

# initial_rev: 14f83e40930806c3f5c61988e69a3ca1820a1b8f
