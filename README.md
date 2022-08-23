# Ansible Configuration Backup Manager
![ansible-network-config-backups-front](https://user-images.githubusercontent.com/29799963/184521743-39d040f1-13ab-497b-a2bd-70849ad74ba9.png)
## Backup configs of many network vendors

## Features

- Daily Ansible Job to backup all network device configs
- Currently Supported Vendors/OS:
  - Opengear
  - ArubaOS
  - Cisco ASA and IOS
  - Fortios
  - Junos
  - Citrix Netscaler
  - Big-IP F5

## Execution Flow
![ansible-network-config-backups-workflow](https://user-images.githubusercontent.com/29799963/184521753-551d56ae-fbc4-49ac-8d2a-ff67c662e41f.png)

### Running the playbook

Here is an example output of running the playbook against 8 hosts each on a different network operating system (the vendors listed above). This playbook has been tested to run on over 1000 network devices in a single execution.

Command:
```sh
[root@ncm]# ansible-playbook -i netbox_inventory.yml -e "var_hosts=aruba1:asa1:f51:nss1:fortios1:ios1:junos1:opengear1" ncm-engine.yml
```
Output:
```sh
PLAY [PLAY TO BACKUP NETWORK CONFIGURATIONS] **********

TASK [delete exisiting successful_hosts file] **********
changed: [aruba1 -> localhost]

TASK [delete exisiting failed_hosts file] **********
changed: [aruba1 -> localhost]

TASK [delete total_hosts file] **********
changed: [aruba1 -> localhost]

TASK [create successful_hosts file] **********
changed: [aruba1 -> localhost]

TASK [create failed_hosts file] **********
changed: [aruba1 -> localhost]

TASK [create total_hosts file] **********
changed: [aruba1 -> localhost]

TASK [update total_hosts file] **********
changed: [aruba1 -> localhost]

TASK [include_role : generate-backups] **********

TASK [generate-backups : include_tasks] **********
included: /root/ncm/roles/generate-backups/tasks/aos-backup-config.yml for aruba1
included: /root/ncm/roles/generate-backups/tasks/asa-backup-config.yml for asa1
included: /root/ncm/roles/generate-backups/tasks/big-ip-backup-config.yml for f51
included: /root/ncm/roles/generate-backups/tasks/citrix-backup-config.yml for nss1
included: /root/ncm/roles/generate-backups/tasks/fortios-backup-config.yml for fortios1
included: /root/ncm/roles/generate-backups/tasks/ios-backup-config.yml for ios1
included: /root/ncm/roles/generate-backups/tasks/junos-backup-config.yml for junos1
included: /root/ncm/roles/generate-backups/tasks/opengear-backup-config.yml for opengear1

TASK [generate-backups : grab and download aruba config] **********
ok: [aruba1]

TASK [generate-backups : Save the backup information.] **********
changed: [aruba1 -> localhost]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [aruba1 -> localhost]

TASK [generate-backups : Backup ASA Device] **********
ok: [asa1]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [asa1 -> localhost]

TASK [generate-backups : grab and download big-ip config] **********
ok: [f51 -> localhost]

TASK [generate-backups : Save the backup information.] **********
changed: [f51 -> localhost]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [f51 -> localhost]

TASK [generate-backups : grab and download citrix config] **********
ok: [nss1]

TASK [generate-backups : Save the backup information.] **********
changed: [nss1 -> localhost]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [nss1 -> localhost]

TASK [generate-backups : Backup Fortigate Device] **********
ok: [fortios1]

TASK [generate-backups : Save the backup information.] **********
changed: [fortios1]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [fortios1 -> localhost]

TASK [generate-backups : Backup IOS Device] *****************
ok: [ios1]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [ios1 -> localhost]

TASK [generate-backups : grab and download junos config] **********
ok: [junos1]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [junos1 -> localhost]

TASK [generate-backups : grab and download opengear config] **********
changed: [opengear1]

TASK [generate-backups : Save the backup information.] **********
ok: [opengear1 -> localhost]

TASK [generate-backups : Add SUCCESS line to file] **********
changed: [opengear1 -> localhost]

PLAY [SYNC NETWORK CONFIGURATIONS TO S3 BUCKET] *************

TASK [delete exisiting s3_sync file] ************************
changed: [localhost]

TASK [create s3_sync file] **********************************
changed: [localhost]

TASK [include_role : sync-to-s3] ****************************

TASK [sync-to-s3 : Sync to S3] ******************************
changed: [localhost]

TASK [sync-to-s3 : Add status to s3 state file] *************
changed: [localhost]

PLAY [Build Email Template] *********************************

TASK [lookup file successful_hosts.txt] *********************
ok: [localhost]

TASK [lookup file failed_hosts.txt] *************************
ok: [localhost]

TASK [lookup file total_hosts.txt] **************************
ok: [localhost]

TASK [lookup file failed_s3.txt] ****************************
ok: [localhost]

TASK [Generate Backup State File] ***************************
changed: [localhost]

TASK [send email] *******************************************
ok: [localhost]

PLAY RECAP **************************************************
asa1 : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
opengear1 : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
nss1 : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
fortios1      : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
aruba1   : ok=11   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ios1 : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
junos1 : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
f51  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[root@ncm]# 
```
