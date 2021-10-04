#!/bin/bash

nohup python experiments/model_main_tf2.py --model_dir=training/reference/ --pipeline_config_path=pipeline_new.config &
