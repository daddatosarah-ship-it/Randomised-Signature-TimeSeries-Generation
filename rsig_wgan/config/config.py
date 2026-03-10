# config.py

# timeseries
n_lags = 10
data_dim = 1
p = 6
q = 10

# bm
bm_samples = 100000
bm_drift = 0.1
bm_std = 0.2

# gbm
gbm_samples = 50000
gbm_drift = 0.0
gbm_std = 1.0
initial_value_gbm = 1.0

# ar
ar_samples = 50000
phi = -0.1
ar_std = 1.0

# hyperparameters
learning_rate = 1e-4
gradient_steps = 5
batch_size = 10000
mc_num = 1000

# rsigw1
reservoir_dim_metric = 80

# sigw1
truncation_depth = 4
normalise = True

# neural_sde
input_dim = 32
hidden_dim = 32
brownian_dim = 1
reservoir_dim_gen = 80
activation = "Sigmoid"

# lstm
inut_dim = 5  # typo mantenuto? "input_dim"?
hidden_dim = 64
num_layers = 2

# data
data_id = "BM"

# generator
generator_id = "NeuralSDE"

# discriminator
discriminator_id = "RSigW1"

# others
trainable_var = True
same_matrices = False
time_homogeneous_readout = False
