#! /usr/bin/env python3
import argparse
import yaml
from uptime_kuma_api import UptimeKumaApi


def delete_monitor(website, existing_monitors, api):
    monitor_id = None
    for monitor in existing_monitors:
        if monitor['name'] == website['url'] and 'state' in website and website['state'] == 'absent':
        #if monitor['name'] == website['url']:
            monitor_id = monitor['id']
            api.delete_monitor(monitor_id)
            print(f"Deleted {website['url']}")


def read_server_list_from_yaml(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        return data.get('websites', [])


def main(inventory):
    api = UptimeKumaApi('http://myuptimekuma.instance.local')
    api.login('admin', 'tt')
    existing_monitors = api.get_monitors()
    for website in inventory:
        delete_monitor(website, existing_monitors, api)
    api.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display server status")
    parser.add_argument("-i", "--inventory", help="Path to the YAML file containing server names", required=True)
    args = parser.parse_args()
    inventory = read_server_list_from_yaml(args.inventory)
    main(inventory)
