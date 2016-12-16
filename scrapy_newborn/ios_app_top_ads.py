#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
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
    ios_top_app_list = []
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    with open('/Users/ning.chen/Desktop/top_offers.txt', 'rb') as f:
        for i in f.readlines()[546:]:
            android_package_name = str(i.split('	')[0]).strip()
            android_package_type = str(i.split('	')[-1]).strip()
            if android_package_type != 'Android':
                ios_top_app_list.append(android_package_name)
        # print ios_top_app_list
    for index,value in enumerate(ios_top_app_list):
        print index, '---', value
    ios_package_name_list = []
    for ios_app in ios_top_app_list:
        response = requests.get('https://itunes.apple.com/lookup?id=%s'%ios_app)
        ios_result = json.loads(response.content)
        # print type(ios_result)

        if ios_result['resultCount'] != 0:
            ios_package_name = ios_result['results'][0]['bundleId']
            ios_package_name_list.append(ios_package_name)
    # print ios_package_name_list
    for index,value in enumerate(ios_package_name_list):
        print index,'---',value
    # public_url = 'https://play.google.com/store/apps/details?id='
    # os.chdir('/Users/ning.chen/Desktop/videos/')
    # a = 1
    # for package in ios_package_name_list[130:]:
    #     print a
    #     print '2' * 150
    #     print package
    #     print '2' * 150
    #     response = urllib2.urlopen(public_url + str(package))
    #     text = unicode(response.read(), "utf-8")
    #     vedio_url, app_tiele_name = parse_html(text)
    #     if vedio_url:
    #         child = subprocess.Popen(
    #             ['youtube-dl', '--proxy', 'localhost:62911', '-o', '%s_%s.mp4' % (app_tiele_name, package),
    #              str(vedio_url)])
    #         time.sleep(10)
    #         a += 1
    # print ios_package_name_list

        # headers = {
        #    'User-Agent': 'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.27.1'
        # }

        # headers = {
        #    'User-Agent': 'Mozilla/5.0 (iPhone;CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46(KHTML,like Gecko) Version/9.0 Moblie/13A340 Safari/601.1'
        # }
        # for ios_id in android_package_list:
        #     public_url = 'https://itunes.apple.com/cn/app/minecraft-pocket-edition/id'+str(ios_id)
        #     req = urllib2.Request(public_url)
        #     req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36')
        #     response = urllib2.urlopen(req)
        #     response_html = response.read()
        #     print response_html
        #     with open('/Users/ning.chen/Desktop/test.html','wt') as f:
        #         f.write(response_html)
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
