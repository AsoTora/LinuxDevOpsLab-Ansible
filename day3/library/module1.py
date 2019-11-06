#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import psutil


def checkIfProcessRunning1(procname):
    for proc in psutil.process_iter():
        try:
            if procname.lower() in proc.name().lower():
                return proc.as_dict(attrs=['name', 'username'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            process=dict(requred=True, type='str')
        )
    )

    process = module.params["process"]

    results = {}
    results.update({
        "process_info": checkIfProcessRunning(process)
    })
    module.exit_json(**results)
main()