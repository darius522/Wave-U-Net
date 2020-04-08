from sacred import Experiment
from Config import config_ingredient
import Evaluate
import os

ex = Experiment('Waveunet Prediction', ingredients=[config_ingredient])

@ex.config
def cfg():
    model_path = os.path.join('./Source_Estimates/use_case_1/waveunet/243653-84000',"243653-84000") # Load stereo vocal model by default
    input_path = os.path.join("test_set_mixes","CSD_LI_mix_22050.wav") # Which audio file to separate
    output_path = './Source_Estimates/use_case_1/waveunet/243653-84000' # Where to save results. Default: Same location as input.

@ex.automain
def main(cfg, model_path, input_path, output_path):
    model_config = cfg["model_config"]
    Evaluate.produce_source_estimates(model_config, model_path, input_path, output_path)