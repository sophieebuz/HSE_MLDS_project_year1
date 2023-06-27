import psutil

import matplotlib
matplotlib.use('agg')
import psutil, datetime
import mpld3
from markupsafe import Markup 
import platform
from matplotlib import pyplot as plt
import numpy
from operator import itemgetter
import threading
import time

mem_info = list()
disk_usage = list()
FIGSIZE=4
UPDATE_FREQ=10
MAX_LENGTH=10
def timer_thread():
    while True:
        time.sleep(UPDATE_FREQ)
        mi = psutil.virtual_memory()
        if mem_info.__len__() >= MAX_LENGTH:
            mem_info.pop(0)
        if disk_usage.__len__() >= MAX_LENGTH:
            disk_usage.pop(0)
        di = list()
        for dp in psutil.disk_partitions():
            try:
                du = psutil.disk_usage(dp.mountpoint)
            except:
                continue
            di.append(du.free / 1024 / 1024)
        mem_info.append([mi.available / 1024 / 1024])
        disk_usage.append(di)

def start():
    t = threading.Thread(target=timer_thread,
                         name="Monitor",
                         args=(),
                         daemon=True)
    t.start()

start()

def get_blocks():
    blocks = list()
    get_mem_info(blocks)
    get_disks_usage(blocks)
    return blocks

def get_mem_info(blocks):
    fig = plt.figure(figsize=(2 * FIGSIZE, FIGSIZE))
    plt.subplot(121)
    mem = psutil.virtual_memory()
    labels = ['Available', 'Used', 'Free']
    fracs = [mem.available, mem.used, mem.free]
    lines = list()
    lines.append(str.format('Avaliable memory: {0} MB',mem.available))
    lines.append(str.format('Used memory: {0} MB', mem.used))
    lines.append( str.format('Free memory: {0} MB', mem.free))
    if psutil.LINUX:
        labels = numpy.hstack((labels, ['Active', 'Inactive', 'Cached', 'Buffers', 'Shared']))
        fracs = numpy.hstack((fracs, [mem.active, mem.inactive, mem.cached, mem.buffers, mem.shared]))
        lines.append(str.format('Active memory: {0} MB', mem.active))
        lines.append(str.format('Inactive memory: {0} MB', mem.inactive))
        lines.append(str.format('Cached memory: {0} MB', mem.cached))
        lines.append(str.format('Buffers memory: {0} MB', mem.buffers))
        lines.append(str.format('Shared memory: {0} MB', mem.shared))
    plt.pie(fracs, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.subplot(122)
    plt.plot(mem_info)
    plt.ylabel('MBs')
    plt.xlabel(str.format('Interval {0} s', UPDATE_FREQ))
    plt.title('Avaliable memory')
    plt.tight_layout()
    graph = mpld3.fig_to_html(fig)
    blocks.append({
            'title': 'Memory info',
            'graph': Markup(graph),
            'data':
                {
                    'primary' : str.format("Total memory: {0} MB", mem.total / 1024 / 1024),
                    'lines' : lines
                }
        })
    print( blocks)

def get_disks_usage(blocks):
    num = 0
    for dp in psutil.disk_partitions():
        fig = plt.figure(figsize=(2 * FIGSIZE, FIGSIZE))
        plt.subplot(121)
        try:
            di = psutil.disk_usage(dp.mountpoint)
        # gets error on Windows, just continue anyway
        except:
            continue
        labels = ['Free', 'Used', ]
        fracs = [di.free, di.used]
        plt.pie(fracs, labels=labels, shadow=True, autopct='%1.1f%%')
        plt.subplot(122)
        plt.plot(list(map(itemgetter(num), disk_usage)))
        plt.ylabel('MBs')
        plt.xlabel(str.format('Interval {0} s', UPDATE_FREQ))
        plt.title('Disk available space')
        plt.tight_layout()
        graph = mpld3.fig_to_html(fig)
        blocks.append({
            'title': str.format('Disk {0} info', dp.mountpoint),
            'graph': Markup(graph),
            'data':
                {
                    'primary': '',
                    'lines': [ str.format('Free memory: {0} MB', di.free / 1024 / 1024),
                               str.format('Used memory: {0} MB', di.used / 1024 / 1024) ]
                }
        })
        num = num + 1