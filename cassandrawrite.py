#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import random
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import time

def write(vl, data=None):
#    get connection from pycassa connection pool 
#    创建keyspace Rawdata保存监控数据
    pool = ConnectionPool('Monitor', ['localhost:9160'])
#   创建columnFamily：RawData, Rollups60, Rollups300, Rollups7200, Rollups86400
    col_fam_rawdata = pycassa.ColumnFamily(pool, 'rawdata')    
    
#   加入时间进行分区,以月作为分区
    timeString = time.strftime("%Y-%m", time.localtime(vl.time))
    key = [str(vl.host), str(vl.plugin), str(vl.plugin_instance), str(vl.type), str(vl.type_instance), timeString]
    keyString = "#".join(key)
    
    
    for i in vl.values:
        col_fam_rawdata.insert(keyString, {vl.time: i})     #插入RawData
        

#   同时写入一个文件作为测试
    with open('/tmp/workfile', 'a') as f:
        f.write(keyString + " " + str(vl.time) + " " + str(i) + "\n")
     
    pool.dispose()
    f.close()
try:
    import collectd
    collectd.register_write(write)
except ImportError:
    pass
