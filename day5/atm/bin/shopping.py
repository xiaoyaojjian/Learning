# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lichengbing

import os, sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src import shopping

"""
购物商城入口：调用ATM结账
"""
if __name__ == '__main__':
    shopping.main()