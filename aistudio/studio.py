# AI Experiment Studio

# config 
from aistudio.utils import ConfigHandler

class AIStudio():
    def __init__(self, train_fn, config, file_name = './AIStudio', tb_path = './tests/test0'):
        self.train_fn = train_fn # external running function
        self.base_conf = config
        self.file_name = file_name # name of the file to write run configs
        self.tb_path = tb_path # path to the tensorboard

        # all the lists to vary for my experiments
        self.configs = [] # list of all the configuration to run the experiments
        self.seeds = [] # list of all the seeds to give to the model
        self.maxlen = [] # list of all maxlen to test
        self.minlen = [] # list of all minlen to test
        self.batch_size = [] # list of all the batchsizes

        assert len(self.maxlen) == len(self.minlen) # to check if we have same sets

    def _make_config(self):
        # function to return the ConfigurationHandler
        cnt = 0
        for seed in self.seeds:
            for maxl, minl in zip(self.maxlen, self.minlen):
                config = ConfigHandler(self.base_conf)
                config.maxlen = maxl
                config.minlen = minl
                config.seed = seed
                config.add('tb_path', self.tb_path)
                config.add('exp_num', cnt)
                cnt += 1

                self.config.append(config)

    def add(self, key, val):
        setattr(self, key, val)

    def run(self):
        for i, config in self.configs:
            config.file_name = '{0}_{1}.txt'.format(self.file_name, i)
            self.train_fn(config)