#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import time


def main():
    for i in itertools.count(1):
        with open('log.txt', 'a') as file:
            line = "%s" % i

            file.write(line)
            print(line)

            file.write('\n')
            time.sleep(1)


if __name__ == "__main__":
    main()
