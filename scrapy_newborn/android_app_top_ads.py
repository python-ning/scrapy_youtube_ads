#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2

import requests
import subprocess
from pyquery import PyQuery as pq
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    android_package_list = []

    with open('/Users/ning.chen/Desktop/top_offers.txt', 'rb') as f:
        for i in f.readlines()[1:]:
            android_package_name = str(i.split('	')[0]).strip()
            android_package_type = str(i.split('	')[-1]).strip()
            if android_package_type != 'ios':
                android_package_list.append(android_package_name)
    # try:
    public_url = 'https://play.google.com/store/apps/details?id='
    os.chdir('/Users/ning.chen/Desktop/videos/')
    a = 1
    for package in android_package_list:
        print a
        print '2' * 150
        print package
        print '2' * 150
        response = urllib2.urlopen(public_url + str(package))
        text = unicode(response.read(),"utf-8")
        vedio_url, app_tiele_name = parse_html(text)
        if vedio_url:
            child = subprocess.Popen(['youtube-dl', '--proxy', 'localhost:62911', '-o', '%s_%s.mp4' % (app_tiele_name, package), str(vedio_url)])
            time.sleep(10)
            a += 1
    # except Exception, e:
    #     print e
    # finally:
    #     print 'jixu'*100
    return 'ok'


def parse_html(response):
    b = pq(response)
    vedio_url = b('span[class="play-action-container"]').attr('data-video-url')
    app_tiele_name = b('div[class="id-app-title"]').text()
    print '1'*150
    print vedio_url
    print app_tiele_name
    print type(app_tiele_name)
    print '1' * 150
    return vedio_url, app_tiele_name


if __name__ == '__main__':
    main()
