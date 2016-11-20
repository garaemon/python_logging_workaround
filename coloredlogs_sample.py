#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

try:
    import coloredlogs
except:
    print 'Install coloredlogs by `pip install coloredlogs`'
    sys.exit(1)

def output_message():
    logging.debug('debug')
    logging.warning('worning')
    logging.info('info')


def main():
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES
    field_styles['levelname'] = {'color': 'white', 'bold': True}
    coloredlogs.install(level=logging.DEBUG,
                        fmt='%(asctime)s [%(levelname)s] %(message)s',
                        field_styles=field_styles)
    output_message()

if __name__ == '__main__':
    main()
