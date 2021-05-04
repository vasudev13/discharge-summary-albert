CONFIG = {
    # PATH TO ZIP FILE
    'ZIP_PATH': './mednli-a-natural-language-inference-dataset-for-the-clinical-domain-1.0.0.zip',
    'UNZIP': False,
    # PATH TO UNZIP DATASET
    'DATA_PATH': '../../datasets/mednli/1.0.0/',
    'sentence1': 'sentence1',
    'sentence2': 'sentence2',
    'labels': 'gold_label',
    'SEED': 13,
    'MAX_LEN': 256,
    'MODEL_NAME_OR_PATH': 'dmis-lab/biobert-v1.1',
    'LEARNING_RATE': 2e-5,
    'ADAM_EPSILON': 1e-8,
    'WEIGHT_DECAY': 0.0,
    'NUM_CLASSES': 3,
    'TRAIN_BS': 32,
    'VAL_BS': 32,
    'WARMUP_STEPS': 0,
    'MAX_EPOCHS': 5,
    'CHECKPOINT_DIR': './checkpoints',
    'NUM_WORKERS': 2,
    'PRECISION': 16,
    'MODEL_SAVE_NAME': 'biobert_v1',
}
