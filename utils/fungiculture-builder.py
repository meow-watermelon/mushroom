#!/usr/bin/env python3

import argparse
import json
import sys
import yaml

class ComposeBuilder:
    """
    class to build Docker Compose configuration
    """

    def __init__(self):
        self.version = None
        self.image = None
        self.network_name = None
        self.cluster_head_node = None
        self.cluster_compute_nodes = set()
        self.compose_config = {}

    def set_version(self, version):
        """
        method: set up Docker Compose template version
        """

        self.version = version
        return self.version

    def set_image(self, image):
        """
        method: set up Docker image name
        """

        self.image = image
        return self.image

    def set_network_name(self, network_name):
        """
        method: set up network name(bridge mode)
        """

        self.network_name = network_name
        return self.network_name

    def set_cluster_head_node(self, cluster_head_node):
        """
        method: set up cluster head node name
        """

        self.cluster_head_node = cluster_head_node
        return self.cluster_head_node

    def set_cluster_compute_nodes(self, cluster_compute_nodes):
        """
        method: set up cluster compute nodes in a set data structure
        """

        self.cluster_compute_nodes = cluster_compute_nodes

        if self.cluster_head_node:
            # remove the compute node if its name is the same as head node
            if self.cluster_head_node in self.cluster_compute_nodes:
                self.cluster_compute_nodes.remove(self.cluster_head_node)
            else:
                pass
        else:
            pass

        return self.cluster_compute_nodes

    def generate_compose_config(self):
        """
        method: construct dict data structure to layout Docker Compose configuration
        """

        self.compose_config = {}

        self.compose_config['version'] = self.version
        self.compose_config['networks'] = {}
        self.compose_config['networks'][self.network_name] = {'driver': 'bridge'}

        # set up nodes
        self.compose_config['services'] = {}

        # head node
        self.compose_config['services'][self.cluster_head_node] = {}
        self.compose_config['services'][self.cluster_head_node]['image'] = self.image
        self.compose_config['services'][self.cluster_head_node]['networks'] = [self.network_name]

        # compute nodes
        for node in self.cluster_compute_nodes:
            self.compose_config['services'][node] = {}
            self.compose_config['services'][node]['image'] = self.image
            self.compose_config['services'][node]['networks'] = [self.network_name]

        return self.compose_config


if __name__ == '__main__':
    # set up command arguments
    parser = argparse.ArgumentParser(description='Mushroom HPC Cluster Docker Compose Configuration Generator')
    parser.add_argument('--version', type=str, required=False, default='3.8', help='Docker Compose template version (default: 3.8)')
    parser.add_argument('--image', type=str, required=True, help='Docker image name')
    parser.add_argument('--network-name', type=str, required=True, help='Docker network name(bridge mode)')
    parser.add_argument('--head-node', type=str, required=True, help='Docker Mushroom HPC head node name')
    parser.add_argument('--compute-nodes', type=str, required=True, help='Docker Mushroom HPC compute node names (example: spore1,spore2,spore3)')
    args = parser.parse_args()

    # initialize config object
    mushroom_dc_config = ComposeBuilder()
    mushroom_dc_config.set_version(args.version)
    mushroom_dc_config.set_image(args.image)
    mushroom_dc_config.set_network_name(args.network_name)
    mushroom_dc_config.set_cluster_head_node(args.head_node)
    mushroom_dc_config.set_cluster_compute_nodes(set(args.compute_nodes.split(',')))

    # generate Docker Compose configuration
    mushroom_dc_config.generate_compose_config()

    # print Docker Compose configuration
    yaml.dump(mushroom_dc_config.compose_config, sys.stdout)
