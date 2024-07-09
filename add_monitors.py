#! /usr/bin/env python3
import argparse
import yaml
from uptime_kuma_api import UptimeKumaApi, MonitorType


def add_monitor(website, existing_monitors, api):
    monitor_exists = any(monitor['name'] == website['url'] for monitor in existing_monitors)
    if not monitor_exists and (website.get('state', None) is None or website.get('state') != 'absent'):
        api.add_monitor(
            type=MonitorType.HTTP,
            name=f"{website['url']}",
            url=f"https://{website['url']}",
            headers={
                "User-Agent": "MyLittleUserAgent"
            },
            notificationIDList=['2'],
            expiryNotification=True,
            ignoreTls=True,
            customSubject='[MONITORING] {{HOSTNAME_OR_URL}} {{STATUS}}'
        )
        print(f"Added {website['url']}...")
    else:
        print(f"Already exists {website['url']}...")


def read_server_list_from_yaml(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        return data.get('websites', [])


def main(inventory):
    api = UptimeKumaApi('http://myuptimekuma.instance.local')
    api.login('admin', 'ttt')
    existing_monitors = api.get_monitors()
    for website in inventory:
        add_monitor(website, existing_monitors, api)
    api.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display server status")
    parser.add_argument("-i", "--inventory", help="Path to the YAML file containing server names", required=True)
    args = parser.parse_args()
    inventory = read_server_list_from_yaml(args.inventory)
    main(inventory)
