#!/usr/bin/env python3

import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger

def move_dataset_files(dataset_files, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for file_path in dataset_files:
        filename = os.path.basename(file_path)
        target_path = os.path.join(target_dir, filename)
        print('move to {}'.format(target_path))
        os.rename(file_path, target_path)

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """

    # TODO: Implement function
    dataset_file_path = os.path.join(data_dir, '*.tfrecord')
    dataset_files = glob.glob(dataset_file_path)
    N = len(dataset_files)

    n_train, n_valid, n_test = int(N*0.6), int(N*0.2), int(N*0.2)

    # Shuffle dataset
    random.shuffle(dataset_files)

    train_files = dataset_files[:n_train]
    valid_files = dataset_files[n_train:n_train+n_valid]
    test_files = dataset_files[n_train+n_valid:]

    train_dir = os.path.join('.', 'data', 'train')
    valid_dir = os.path.join('.', 'data', 'valid')
    test_dir = os.path.join('.', 'data', 'test')

    move_dataset_files(train_files, train_dir)
    move_dataset_files(valid_files, valid_dir)
    move_dataset_files(test_files, test_dir)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)
