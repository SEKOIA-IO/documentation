
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "AUD_It"

    ```
	AUD_It audit Pipin root OK 16 sep 2022 15:42:41.885007 No associated roles cmd: 1 arg: 0
    ```



=== "AUD_Proc"

    ```
	AUD_Proc cron root root OK 25 sep 2022 23:10:00.924334 No associated roles pid: 0 cmd: 5
    ```



=== "CRON_Finish"

    ```
	CRON_Finish cron root root OK 25 sep 2022 23:00:00.861158 No associated roles user = root pid = 3932756 time = Sun Sep 25 23:00:00 2022
    ```



=== "CRON_Start"

    ```
	CRON_Start cron root root OK 17 sep 2022 00:00:00.139458 No associated roles event = start cron job cmd = /usr/share/centrifydc/bin/logrotate.sh 2>&1 >> /var/log/centrify_logrotate.log time = Sat Sep 17 00:00:00 2022
    ```



=== "FILE_Link"

    ```
	FILE_Link dad root root OK 31 jul 2022 14:02:33.696402 No associated roles linkname /usr/bin/cdax/bsh filename /usr/bin/cdax/ksh93
    ```



=== "FILE_Link2"

    ```
	filename /bin/cdax/ksh FILE_Link dad root root OK 31 jul 2022 15:02:33.597401 No associated roles
    ```



=== "FILE_Pipe"

    ```
	  FILE_Pipe Pipin root admin OK 10 Nov 2022 09:21:53.955363 No associated roles read: 7 write: 8
    ```



=== "FILE_Read"

    ```
	FILE_Read tar Pipin root OK 10 Nov 2022 09:30:12.229710 No associated roles file descriptor = 1635083369 filename = t object read event detected /app1/coresec/active/BEKAL-CORE-01S.p12
    ```



=== "FILE_Rename"

    ```
	FILE_Rename BESClient root root OK 25 sep 2022 22:33:21.081155 No associated roles frompath: /var/opt/BESClient/besclient.config.tmp topath: /var/opt/BESClient/besclient.config
    ```



=== "FILE_Stop"

    ```
	SRC_Start srcmstr root root OK 21 sep 2022 00:00:08.467005 No associated roles syslog_ng
    ```



=== "FILE_Unlink"

    ```
	FILE_Unlink Pipin root root OK 25 sep 2022 23:14:20.756159 No associated roles filename /var/adm/nim/glock
    ```



=== "FS_Chroot"

    ```
	FS_Chroot sshd root root OK 23 sep 2022 17:14:21.748158 No associated roles change root directory to: /var/empty
    ```



=== "FS_Mkdir"

    ```
	FS_Mkdir Pipin root root OK 25 sep 2022 23:04:23.825394 No associated roles mode: 755 dir: /var/adm/nim/6292044
    ```



=== "FS_Rmdir"

    ```
	FS_Rmdir rm root root OK 25 sep 2022 23:14:20.859389 No associated roles remove of directory: /var/adm/nim/6292046
    ```



=== "PROC_Adjtime"

    ```
	PROC_Adjtime xntpd root root OK 25 sep 2022 21:57:37.226128 No associated roles old time: 01 jan 1970 01:00:00.1664135, delta: 226172812:0
    ```



=== "PROC_Execute"

    ```
	PROC_Execute    sh                              root     Pipin FAIL          22 Nov 2022 10:20:32.056053  No associated roles                      euid: 503 egid: 403 epriv: 0:0 name sh -c /app/DB2/11.1/instance/db2iset -i Pipin DB2AUTOSTART 2>&1 
    ```



=== "PROC_Kill"

    ```
	PROC_Kill rsyslogd root root OK 25 sep 2022 23:14:20.816166 No associated roles pid: 3605020, sig: 22
    ```



=== "PROC_LoadError"

    ```
	PROC_LoadError perl5.28.1 root root FAIL 25 sep 2022 23:12:21.397204 No associated roles flags: 80, libpath: , file: /usr/lib/nls/loc/C C C C C C
    ```



=== "PROC_RealGID"

    ```
	PROC_RealGID rm_mlcache_file root root OK 25 sep 2022 21:13:31.584159 No associated roles old rgid: 0, new gid: 0, which: egid
    ```



=== "PROC_SetGroups"

    ```
	PROC_SetGroups cron root root OK 25 sep 2022 23:00:00.835203 No associated roles group set: system,bin,sys,security,cron,audit,lp,ivmgr,apache
    ```



=== "PROC_SetUserIDs"

    ```
	PROC_SetUserIDs db2fm                           root     db2inst1 OK          22 Nov 2022 14:19:42.790048  No associated roles                      effect: 503, real: 503, saved: -1, login: -1#012
    ```



=== "PROC_SetUserIDs_processtty_no_#"

    ```
	PROC_SetUserIDs db2fm                           root     db2inst1 OK          22 Nov 2022 14:19:42.790048  No associated roles                      effect: 503, real: 503, saved: -1, login: -1012
    ```



=== "PROC_Sysconfig"

    ```
	PROC_Sysconfig exportfs root root OK 25 sep 2022 23:14:20.836155 No associated roles 3
    ```



=== "S_PASSWD_READ"

    ```
	S_PASSWD_READ cron root root OK 25 sep 2022 23:10:00.924334 No associated roles audit object read event detected /etc/security/passwd
    ```



=== "S_USER_WRITE"

    ```
	S_USER_WRITE vi Pipin root OK 21 sep 2022 10:26:12.893117 No associated roles audit object write event detected /etc/security/user
    ```



=== "TCP_kaccept"

    ```
	TCP_kaccept Pipin root root OK 25 sep 2022 23:09:25.544152 No associated roles fd14 Port 10.30.134.100 1022 kx5frsip01-a nimaux
    ```



=== "TCP_kbind"

    ```
	TCP_kbind Pipin root root OK 25 sep 2022 23:14:20.826159 No associated roles fd11 /dev/.SRC-unix/SRC0006292046YEya
    ```



=== "TCP_klisten"

    ```
	TCP_klisten Pipin root root OK 31 jul 2022 10:21:24.798402 0 fd15 qlimit 1
    ```



=== "USER_1"

    ```
	from hostname: unix: The privilege command /usr/sbin/lspath, is executed by user with id 501
    ```



=== "USER_Login"

    ```
	flags: 80, libpath: , file: /usr/lib/security/DCE USER_Login sshd root root OK 29 jul 2022 09:58:03.091427 No associated roles
    ```



=== "USER_Login2"

    ```
	USER_Login      db2ckpw                         root     Pipin OK          22 Nov 2022 13:41:34.586022  No associated roles                      user: Pipin tty: #012
    ```



