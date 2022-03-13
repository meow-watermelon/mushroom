FROM alpine:latest

LABEL "maintainer"="Hui Li"
LABEL "description"="Mushroom HPC Cluster Image"
LABEL "version"="0.0.1"

USER root

COPY ./bin /sbin

RUN ["/sbin/mushroom-bootstrap.sh"]

# allow root user to run mpirun
ENV OMPI_ALLOW_RUN_AS_ROOT=1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

# set up SSH passwordless environment
COPY --chown=root:root shared-storage/root_ssh_dir /root/.ssh/
COPY --chown=root:root shared-storage/sshd_config /etc/ssh/
COPY --chown=root:root shared-storage/ssh_config /etc/ssh/

# start sshd daemon
ENTRYPOINT ["/bin/sh", "/sbin/ssh-entrypoint.sh"]

# keep alive
CMD while true; do sleep 86400; done
