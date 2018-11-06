#!/bin/bash
# this script will start Pd in no gui mode
# this script should go into /etc/profile.d/
# the ownership should be root:root (chown root:root)
# the permissions should be (chmod 755)

sudo -H -u pi bash -c bash "echo 'starting Pd now'"
pd -nogui /home/pi/loppi/step-vibrato.pd &

/home/pi/loppi/lop2pd.py &
