# -*- coding: utf-8 -*-
import subprocess

# nslookup命令用于查询DNS的记录，查看域名解析是否正常，在网络故障的时候用来诊断网络问题

# $ nslookup www.python.org
# Server:		10.201.4.4
# Address:	10.201.4.4#53
#
# Non-authoritative answer:
# www.python.org	canonical name = dualstack.python.map.fastly.net.
# Name:	dualstack.python.map.fastly.net
# Address: 151.101.76.223
#
# Exit code: 0
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ jps')
res = subprocess.call(['jps', '-ml'])
print('jps exit code:', res)

import subprocess

# 上面的代码相当于在命令行执行命令nslookup，然后手动输入:
# set q=mx
# python.org
# exit
print('$ nslookup')
# process 通信的另一种方式：Pipe
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# q=mx, 邮件服务器记录
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
