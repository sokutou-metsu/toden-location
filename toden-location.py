# -*- coding: utf-8-unix -*-
u"""都電荒川線の運行情報を取得する
"""
import argparse
from bs4 import BeautifulSoup
from cssutils import parseStyle
import csv
from datetime import datetime
import logging
import os.path
import requests

import _resource as resource

RESOURCE_URL = 'http://tobus.jp/tlsys/navi?VCD=csapproach&ECD=reload&LCD=&TTC=&STC='


class Car(object):
    u"""電車情報
    """
    def __init__(self, **kwargs):
        self._attributes = {}
        for k, v in kwargs.items():
            self._attributes[k] = v
        return

    @property
    def car_id(self):
        return self._attributes.get('car_id', None)

    @property
    def status(self):
        return self._attributes.get('status', None)

    @property
    def current_stop(self):
        return self._attributes.get('current_stop', None)

    @property
    def next_stop(self):
        return self._attributes.get('next_stop', None)

    @property
    def destination(self):
        return self._attributes.get('destination', None)

    @property
    def direction(self):
        return self._attributes.get('direction', None)

    @property
    def update_time(self):
        return self._attributes.get('update_time', None)

    def __str__(self):
        current_stop = resource.get_stop_name(self.current_stop)
        if self.next_stop is None:
            position = current_stop
        else:
            next_stop = resource.get_stop_name(self.next_stop)
            position = u'{0}→{1}'.format(current_stop, next_stop)
        update_time = ''
        if self.update_time is not None:
            update_time = ' ({0})'.format(self.update_time.strftime('%H:%M'))
        return u'[{0}] {1} ＜{2}行き＞{3}'.format(
            self.car_id, position, resource.get_stop_name(self.destination),
            update_time)


def output_as_csv(cars, output_file):
    FIELD_NAMES = ['date', 'time', 'car_id', 'status',
                   'current_stop', 'next_stop', 'direction', 'destination']

    def make_record(car):
        r = {}
        update_time = car.update_time
        r['date'] = update_time.strftime('%Y/%m/%d')
        r['time'] = update_time.strftime('%H:%M')
        r['car_id'] = car.car_id
        r['status'] = car.status
        r['current_stop'] = car.current_stop
        r['next_stop'] = car.next_stop
        r['direction'] = car.direction
        r['destination'] = car.destination
        return r

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, FIELD_NAMES, extrasaction='ignore')
        writer.writerows([make_record(car) for car in cars])
    return


def parse_tag(tag, update_time):
    obj = {}

    # 車両番号
    if not tag.has_attr('src'):
        logging.error('no "src" attribute: %s', tag)
        return None
    car_id, _ = os.path.splitext(os.path.basename(tag['src']))
    obj['car_id'] = car_id

    # 位置
    if not tag.has_attr('style'):
        logging.error('no "style" attribute: %s', tag)
        return None
    style = parseStyle(tag['style'])
    top = style.getProperty('top').propertyValue
    if top.length == 0:
        logging.error('no css style "top": %s', tag)
        return None
    left = style.getProperty('left').propertyValue
    if left.length == 0:
        logging.error('no css style "left": %s', tag)
        return None
    pos = resource.get_position(top[0].value, left[0].value)
    if pos is None:
        logging.error('undefined position: <top=%d, left=%d>',
                      top[0].value, left[0].value)
        return None
    obj['status'] = pos[0]
    obj['direction'] = pos[1]
    obj['current_stop'] = pos[2]
    if pos[3] is not None:
        obj['next_stop'] = pos[3]

    # 行先
    if not tag.has_attr('title'):
        logging.error('no "title" attribute: %s', tag)
        return None
    if not tag['title'].startswith(u'行先：'):
        logging.error('"title" attribute is not destination: %s', tag)
        return None
    dest = tag['title'].replace(u'行先：', '').replace(u'行き', '')
    obj['destination'] = resource.find_stop_code(dest)

    # 更新日時
    obj['update_time'] = update_time

    return Car(**obj)


def fetch_time(html):
    tbl = html.select('form.submit_form > table')
    if len(tbl) == 0:
        return None
    td = tbl[0].find('td')
    if td is None:
        return None
    if td.img['src'] != 'pc/images/search/i_time.gif':
        return None
    try:
        t = datetime.strptime(td.get_text(strip=True), u'%Y年%m月%d日 %H:%M')
    except ValueError:
        return None
    return t


def fetch(input_file, output_file):
    if input_file:
        logging.info('from file: %s', input_file)
        with open(input_file, 'r') as f:
            html = BeautifulSoup(f)
    else:
        logging.info('from tobus.jp')
        r = requests.get(RESOURCE_URL)
        html = BeautifulSoup(r.text)

    update_time = fetch_time(html)
    if update_time is None:
        logging.error('cannot find update time')
        return None

    cars = []

    for tag in html.find_all('script'):
        for line in tag.text.splitlines():
            if '<img ' not in line or 'class="den"' not in line:
                continue
            if 'null.png' in line:
                continue

            tag = BeautifulSoup(line.split("'", 3)[1]).img
            if tag is None:
                logging.warning('expected <img> but got: %s', line)
                continue

            car = parse_tag(tag, update_time)
            if car is not None:
                cars.append(car)

    cars.sort(key=lambda x: x.car_id)

    if output_file:
        output_as_csv(cars, output_file)
    else:
        for c in cars:
            print(c)

    return


def main():
    parser = argparse.ArgumentParser(description=u'toden')
    parser.add_argument('-i', '--input', type=str,
                        help='input from file')
    parser.add_argument('-o', '--output', type=str,
                        help='output to file')

    args = parser.parse_args()
    fetch(args.input, args.output)
    return 0


if __name__ == '__main__':
    main()
