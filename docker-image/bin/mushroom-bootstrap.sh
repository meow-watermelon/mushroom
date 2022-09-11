#!/bin/sh

set -e
set -x

echo "### Unlocking root user ... ###"
/usr/bin/passwd -u root || /bin/true

echo "### Installing system packages ... ###"
/sbin/apk add --no-cache openrc openssh build-base
/sbin/rc-update add sshd
/bin/rc-status

/bin/touch /run/openrc/softlevel

/bin/mkdir -m 700 /root/.ssh

echo "### Installing OpenMPI package ... ###"
/sbin/apk add --no-cache openmpi openmpi-dev

echo "### Installing math libraries ... ###"

echo "### Downloading STREAM package ... ###"
/usr/bin/wget https://www.cs.virginia.edu/stream/FTP/Code/Versions/stream_mpi.c -O /root/stream_mpi.c

echo "### Compiling and installing STREAM package ... ###"
/usr/bin/mpicc -O3 -ffreestanding -openmp -mcmodel=medium -Wrestrict -DSTREAM_ARRAY_SIZE=80000000 -DNTIMES=20 -DVERBOSE /root/stream_mpi.c -o /bin/stream_mpi
