# utils file having the config handler

# class for configurations
class ConfigHandler():
    def __init__(self, config_dict):
        # rather than individually setting the values, iterate
        for k, v in config_dict.items():
            setattr(self, k, v)

    def add(self, key, val):
        setattr(self, key, val)

    def set_val(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_txt(self):
        t_ =  '***** CONFIGURATION *****\n'
        t_ += 'seed value: {}\n'.format(config.seed)
        t_ += 'maxlen:     {}\n'.format(config.maxlen)
        t_ += 'minlen:     {}\n'.format(config.minlen)
        t_ += 'batch size: {}\n'.format(config.batch_size)
        t_ += 'epochs:     {}\n'.format(config.num_epochs)
        t_ += 'gen-pre-n:  {}\n'.format(config.gen_pre_train)
        t_ += 'dis-pre-n:  {}\n'.format(config.dis_pre_train)
        t_ += '*************************\n'.format(config.gen_pre_train)