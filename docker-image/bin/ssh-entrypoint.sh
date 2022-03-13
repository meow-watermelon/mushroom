#!/bin/sh

set -e
set -x

/etc/init.d/sshd restart
exec "$@"
