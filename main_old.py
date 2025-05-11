import tkinter as tk
from src.streaming import start_stream, stop_stream
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import neurokit2 as nk


def on_stop():
    # stop_stream now returns (data_anc, data_default, data_aux)
    data_anc, data_default, data_aux = stop_stream()

    if data_anc is None:
        messagebox.showwarning("No Data", "Nothing was streamed.")
        return

    # Plot EDA
    eda = data_anc[:,ANCILLARY['eda_channels'][0]]
    signals_eda, info_eda = nk.eda_process(eda, sampling_rate=ANCILLARY["sampling_rate"])
    nk.eda_plot(signals_eda, info_eda)
    # plt.show()

    # Plot PPG
    ppg = data_aux[:,AUXILIARY['ppg_channels'][0]]
    signals_ppg, info_ppg = nk.ppg_process(ppg, sampling_rate=AUXILIARY["sampling_rate"])
    nk.ppg_plot(signals_ppg, info_ppg)
    plt.show()
    

def on_stop():
    # Stop the background stream and get your data arrays back
    data_anc, data_default, data_aux = stop_stream()

    if data_anc is None:
        messagebox.showwarning("No Data", "Nothing was streamed.")
        return

     # Plot EDA
    eda = data_anc[:,ANCILLARY['eda_channels'][0]]
    signals_eda, info_eda = nk.eda_process(eda, sampling_rate=ANCILLARY["sampling_rate"])
    nk.eda_plot(signals_eda, info_eda)
    # plt.show()

    # Plot PPG
    ppg = data_aux[:,AUXILIARY['ppg_channels'][0]]
    signals_ppg, info_ppg = nk.ppg_process(ppg, sampling_rate=AUXILIARY["sampling_rate"])
    nk.ppg_plot(signals_ppg, info_ppg)
    plt.show()

def main():
    root = tk.Tk()
    root.title("Emotibit Streamer")

    tk.Button(
        root,
        text="▶️Start",
        width=20,
        command=start_stream
    ).pack(padx=10, pady=(10, 5))

    tk.Button(
        root,
        text="⏹Stop",
        width=20,
        command=stop_stream
    ).pack(padx=10, pady=(5, 10))

    root.mainloop()

if __name__ == "__main__":
    main()