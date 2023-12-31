#!/usr/bin/env python
# encoding: utf-8
"""
@author: hongwei zhang
@contact: zhanghwei@sjtu.edu.cn
@file: main_stl_cifar.py
@time: 2022/3/8 15:55
"""
import argparse
import os
from solver_stl_cifar import Solver
from torch.backends import cudnn
from data_loader_cifar import get_loader
from torchvision import transforms
from torchvision.datasets import cifar
from torch.utils.data import DataLoader


def str2bool(v):
    return v.lower() in 'true'


def main(config):
    stl_loader, cifar_loader = get_loader(config)

    solver = Solver(config, stl_loader, cifar_loader)
    cudnn.benchmark = True

    # create directories if not exist
    if not os.path.exists(config.model_path):
        os.makedirs(config.model_path)
    if not os.path.exists(config.sample_path):
        os.makedirs(config.sample_path)

    if config.mode == 'train':
        solver.train()
    elif config.mode == 'sample':
        solver.sample()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # model hyper-parameters
    parser.add_argument('--image_size', type=int, default=32)
    # parser.add_argument('--image_size', type=int, default=28)
    parser.add_argument('--g_conv_dim', type=int, default=64)
    parser.add_argument('--d_conv_dim', type=int, default=64)
    parser.add_argument('--use_reconst_loss', required=True, type=str2bool)
    parser.add_argument('--use_labels', required=True, type=str2bool)
    parser.add_argument('--num_classes', type=int, default=10)

    # training hyper-parameters
    parser.add_argument('--train_iters', type=int, default=40000)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--num_workers', type=int, default=2)
    parser.add_argument('--lr', type=float, default=0.0002)
    parser.add_argument('--beta1', type=float, default=0.5)
    parser.add_argument('--beta2', type=float, default=0.999)

    # misc
    parser.add_argument('--mode', type=str, default='train')
    parser.add_argument('--model_path', type=str, default='./models')
    parser.add_argument('--sample_path', type=str, default='./samples')
    parser.add_argument('--cifar_path', type=str, default='./cifar')
    parser.add_argument('--stl_path', type=str, default='./stl')
    parser.add_argument('--log_step', type=int, default=10)
    parser.add_argument('--sample_step', type=int, default=500)

    config = parser.parse_args()
    print(config)
    main(config)

