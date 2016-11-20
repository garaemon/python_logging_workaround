#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

def output_message():
    logging.debug('debug')
    logging.warning('worning')
    logging.info('info')


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s')
    output_message()

if __name__ == '__main__':
    main()
