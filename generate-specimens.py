#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to generate LevelDB database test files using py-leveldb."""

import os

import leveldb


if __name__ == '__main__':
  specimens_path = os.path.join('specimens', 'leveldb')

  os.makedirs(specimens_path, exist_ok=True)

  database_path = os.path.join(specimens_path, 'database1')
  database = leveldb.LevelDB(database_path)
  # Generate many keys so that a sorted tables file is created.
  for index in range(100000):
    key = f'key{index:d}'.encode('ascii')
    value = f'value{index:d}'.encode('ascii')
    database.Put(key=key, value=value)

  database_path = os.path.join(specimens_path, 'database2')
  database = leveldb.LevelDB(database_path)
  # Generate many keys so that a sorted tables file is created.
  for index in range(100000):
    key = f'key{index:d}'.encode('ascii')
    value = f'value{index:d}'.encode('ascii')
    database.Put(key=key, value=value)

    database.Delete(key)

  database_path = os.path.join(specimens_path, 'database3')
  database = leveldb.LevelDB(database_path)
  # Generate many keys so that a sorted tables file is created.
  for index in range(100000):
    key = f'key{index:d}'.encode('ascii')
    value = f'value{index:d}'.encode('ascii')
    database.Put(key=key, value=value)

    database.Delete(key)

    value = f'new value{index:d}'.encode('ascii')
    database.Put(key=key, value=value)

