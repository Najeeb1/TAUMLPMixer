# configs.py

class Configs:
    def __init__(self):
        # Input settings
        self.c_in = 64
        self.seq_len = 10
        self.pred_len = 10

        # Model architecture settings
        self.e_layers = 3
        self.n_heads = 8
        self.d_model = 512
        self.d_ff = 2048

        # Dropout rates
        self.dropout = 0.1
        self.fc_dropout = 0.1
        self.head_dropout = 0.1

        # Individual settings
        self.individual = True

        # Patch settings
        self.patch_len = 10
        self.stride = 8
        self.padding_patch = 0

        # RevIn settings
        self.revin = True
        self.affine = True
        self.subtract_last = False

        # Decomposition settings
        self.decomposition = True
        self.kernel_size = 3

# To use the configuration, create an instance of the Configs class
# configs = Configs()
