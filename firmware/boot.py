from kmk.bootcfg import bootcfg
# import usb_hid
# usb_hid.enable((usb_hid.Device.KEYBOARD,))

bootcfg(
    usb_id={'manufacturer': "krunchiekrunch", 'product': "krunchboard-90"},
)