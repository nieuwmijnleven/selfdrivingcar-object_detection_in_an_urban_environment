#!/bin/bash

nohup python experiments/model_main_tf2_tpu.py --model_dir=training/reference/ --pipeline_config_path=pipeline_new.config &
