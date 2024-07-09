#! /usr/bin/env python3
import sys
import argparse
import yaml
from uptime_kuma_api import UptimeKumaApi, MonitorType, SMTP


def test_notification(api):
    api.test_notification(
        name="email_this",
        type=SMTP,
    )


def read_server_list_from_yaml(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        return data.get('websites', [])


def main(inventory):
    api = UptimeKumaApi('http://myuptimekuma.instance.local')
    api.login('admin', 'tt')
    test_notification(api)
    api.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display server status")
    parser.add_argument("-i", "--inventory", help="Path to the YAML file containing server names", required=True)
    args = parser.parse_args()
    inventory = read_server_list_from_yaml(args.inventory)
    main(inventory)
