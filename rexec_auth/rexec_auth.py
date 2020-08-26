#!/usr/bin/env python3

import os
import argparse
from pkg_resources import resource_filename
#DOCKERFILE = '~/Documents/WorkStuff/datahub/rexec/rexec_auth/Dockerfile' #FIX TO NOT HARD CODE!

# Could put below into a config file?
GOOGLE_CLIENT_ID = '63104651415-ppiue598slb8asfs4umnqcnvbj4chtid.apps.googleusercontent.com'
GOOGLE_CLIENT_SSECRET = 'tYlMfYNw4zgaQ7Z4wRI5zFqm'

def main():

    args = parse_arguments()

    dockerfile = resource_filename('rexec_auth', 'Dockerfile')
    cmd = f"docker build . --file {dockerfile} -t rexec_auth"
    print(cmd)
    os.system(cmd)

    # http://127.0.0.1:53682

    alias = args.cloud if args.alias is None else args.alias

    if args.cloud == 'google_drive':
        scope = 'drive.readonly' if args.readonly else 'drive'
        if args.rclone_creds:
            rclone_cmd = f'rclone config create {alias} drive scope {scope} config_is_local false'
        else:
            rclone_cmd = f'rclone config create {alias} drive scope {scope} client_id {GOOGLE_CLIENT_ID} client_secret {GOOGLE_CLIENT_SSECRET} config_is_local false'

    run_cmd = f'docker run --rm -it -v ~/.rexec/:/root/.config/rclone/ rexec_auth {rclone_cmd}'
    print(run_cmd)
    os.system(run_cmd)

    # elif cloud == 'dropbox':
    #     if args.readonly:
    #         print("Readonly not supported for Dropbox, creating with write privalleges too")
    #     cmd = f'rclone '


def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('cloud', choices=['google_drive', 'dropbox'])
    parser.add_argument('--alias', '-a', help='Specify internal alias to use for cloud drive (defaults to cloud storage name)')
    parser.add_argument('--readonly', '-r', action='store_true', help='Make credientials to drive readonly')
    parser.add_argument('--rclone_creds', action='store_true')

    return parser.parse_args()


if __name__ == '__main__':
    main()
