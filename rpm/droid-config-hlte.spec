%define device hlte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy Note 3

%define dcd_path ./

%define pixel_ratio 1.8

%define remove_modem 1


%include droid-configs-device/droid-configs.inc

%pre
if [ "$1" = "2" ]; then
  rm /etc/acdbdata/ -r
fi
