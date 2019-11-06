#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from ansible.module_utils.basic import *

import socket
from contextlib import closing
import re
import sys
import os
import json
import psutil


def check_socket(port, host='localhost'):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return True
    return False


def check_content(url, regex):
    regexp = re.compile(r'{}'.join(regex))
    if regexp.search(url):
        return True
    return False


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return proc.as_dict(attrs=['pid', 'name', 'username'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(required=True, type='str'),
            port=dict(requred=True, type='int'),
            url=dict(requred=True, type='str'),
            regex=dict(requred=True, type='str'),
            process=dict(requred=True, type='str'),
        )
    )

    msg = module.params["msg"]
    port = module.params["port"]
    url = module.params["url"]
    regex = module.params["regex"]
    process = module.params["process"]

    results = {}
    results.update({
        "changed": True,
        "msg": msg,
        "listen_mode": check_socket(port),
        "web_content": check_content(url, regex),
        "process_info": checkIfProcessRunning(process)
    })
    module.exit_json(**results)


# include magic from lib/ansible/module_common.py
# <<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
