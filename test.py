import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'src')))
import neurokit2 as nk
import numpy as np
from config import ANCILLARY, AUXILIARY
import time
from brainflow.board_shim import BoardShim, BoardIds, BrainFlowInputParams, BrainFlowPresets
import pandas as pd
import matplotlib.pyplot as plt


params = BrainFlowInputParams()
board_id = BoardIds.EMOTIBIT_BOARD.value

board = BoardShim(board_id, params)
BoardShim.enable_dev_board_logger()

print("Preparing session...")
board.prepare_session()
board.start_stream()

print("Streaming for 30 seconds")
time.sleep(30)

data_default = board.get_board_data(preset=BrainFlowPresets.DEFAULT_PRESET).T
data_aux = board.get_board_data(preset=BrainFlowPresets.AUXILIARY_PRESET).T
data_anc = board.get_board_data(preset=BrainFlowPresets.ANCILLARY_PRESET).T


board.stop_stream()
board.release_session()
print("Streaming stopped")

eda = data_anc[:,ANCILLARY['eda_channels'][0]]
timestamps = data_anc[:,ANCILLARY['timestamp_channel']]

plt.plot(timestamps, eda)
plt.title("EDA RAW")
signals, info = nk.eda_process(eda, sampling_rate=ANCILLARY["sampling_rate"])
plt.plot(timestamps, signals["EDA_Clean"], label="SCR")
plt.title("SCR")