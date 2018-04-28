ansible_postgres_install
=========

A role to install PostgreSQL Master-Slave Replication cluster. 

Requirements
------------

This role will install both Master and slave in parallel. Although this role can be used indivudually (not tested), it's originally designed to work in tandem as a pair. Since PostgreSQL support multiple slave nodes, should be able to run with multiple master_node='no'. 


Role Variables
--------------

The list of variables defined in the 

| Variable Name  | Description | Required (Y/N) | Default Set (Y/N)
|----------------|---|---|---|
| mater_node  | Select 'yes' or 'no' to select master node or the slave node. | Y | N 
| pg_master  | Listening IP address of the master node | Y | N 
| pg_slave  | Listening IP address of the slave node | Y | N 
| pg_version  | PostgreSQL versions, supported 9.4, 9.5, 9.6 and 10 (Defaults to 10)  | Y | Y 
| pg_port       | Port (default 5432) | N | Y
| pg_interface       | Listening interface of the PostgreSQL server. | Y
| pg_lvm  | Volume group name. (Default postgres) | N | Y
| pg_pvs  | Physical disk path. (Default /dev/sdb) | N | Y
| pg_data_lv  | PGDATA filesystem logical volume. (Default pgdatalv) | N | Y
| pg_log_lv  | Postgres Log filesystem logical volume. (Default /dev/sdb) | N | Y
| pg_data  | PGDATA path. (Default /postgres/data) | N | Y
| pg_log  | Postgres Log path. (Default /postgres/archivelog) | N | Y
| pg_fs_type  | Filesystem type for the new filesystems creates. (Default ext4) | N | Y
| pg_owner | PostgreSQL process owner (Default postgres) | N | Y
| pg_group  |PostgreSQL process group. (Default postgres) | N | Y
| pg_replica_user  | PostgreSQL replica user name. (Default replica) | N | Y
| pg_replica_password  | PostgreSQL replica user password. (Default password) | N | Y


Example Playbook
----------------

For a single Master-Slave cluster, the following inventory can be used.

```
[pgcluster]
pgmaster ansible_host=10.152.0.2 master_node='yes' pg_slave='10.152.0.3' 
pgslave ansible_host=10.152.0.3 master_node='no' pg_master='10.152.0.2' 
```

The following playbook will install a Master-Slave cluster on the above two nodes.

```
---

- name: install pg cluster
  hosts: pgcluster
  become: yes
  become_method: sudo
  roles:
    - ansible_postgresql_install
```

License
-------

MIT

Author Information
------------------

Written by Kosala Atapattu (kosala@kosala.net)
