# Word Matters: What Influences Domain Adaptation in Summarization?
This repository contains the source code for _Word Matters: What Influences Domain Adaptation in Summarization?_ accepted by ACL2024. This paper explores the factors influencing domain adaptation performance for LLMs and focuses on the impact of words in training data on summarization tasks. We propose measuring dataset learning difficulty through word-based compression rate and abstraction level. The experiments reveal an approximately linear relationship between cross-domain overlap and performance gain in summarization tasks, independent of the word count. This finding enables predicting model performance on unknown domains without training.
You can measure your own dataset using the python files we provide.

To finetune or evaluate LLMs we use LLama-factory. We also provide the code in this repository. You can follow the instructions of the origin repository. (https://github.com/hiyouga/LLaMA-Factory)

Here is our configration. You can follow it or design your own one.

USE_MODELSCOPE_HUB=1 accelerate launch src/train_bash.py \
    --stage sft \
    --do_train True \
    --model_name_or_path path\
    --finetuning_type lora \
    --template alpaca \
    --dataset_dir data \
    --dataset dataset \
    --cutoff_len 2048 \
    --learning_rate 2e-05 \
    --num_train_epochs 1.0 \
    --max_samples 100000 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 100 \
    --eval_steps 1000 \
    --save_steps 5000 \
    --warmup_steps 0 \
    --neftune_noise_alpha 0 \
    --lora_rank 8 \
    --lora_dropout 0.1 \
    --lora_target q_proj,v_proj \
    --output_dir saves \
    --bf16 True \
    --val_size 0.1 \
    --evaluation_strategy steps \
    --eval_steps 5000 \
    --load_best_model_at_end True \
    --plot_loss True 
