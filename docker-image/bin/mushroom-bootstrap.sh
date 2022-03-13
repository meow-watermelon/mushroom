#!/bin/sh

set -e
set -x

echo "### Unlocking root user ... ###"
/usr/bin/passwd -u root

echo "### Installing system packages ... ###"
/sbin/apk add --no-cache openrc openssh
/sbin/rc-update add sshd
/bin/rc-status

/bin/touch /run/openrc/softlevel

/bin/mkdir -m 700 /root/.ssh

echo "### Installing OpenMPI package ... ###"
/sbin/apk add --no-cache openmpi

echo "### Installing math libraries ... ###"

echo "### Downloading STREAM package ... ###"

echo "### Compiling and installing STREAM package ... ###"
