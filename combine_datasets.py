import pandas as pd
import numpy as np

feb19 = pd.read_csv('data/raw/19feb.csv')
mar19 = pd.read_csv('data/raw/19march.csv')
april19 = pd.read_csv('data/raw/19april.csv')
may19 =  pd.read_csv('data/raw/19may.csv')
june19 = pd.read_csv('data/raw/19june.csv')

feb20 = pd.read_csv('data/raw/20feb.csv')
mar20 = pd.read_csv('data/raw/20march.csv')
april20 = pd.read_csv('data/raw/20april.csv')
may20 = pd.read_csv('data/raw/20may.csv')
june20 = pd.read_csv('data/raw/20june.csv')

feb19tojune19 = pd.concat([feb19, mar19, april19, may19, june19], ignore_index=True)
feb20tojune20 = pd.concat([feb20, mar20, april20, may20, june20], ignore_index=True)

feb19tojune19.to_csv('data/comb/feb19tojune19.csv')
feb20tojune20.to_csv('data/comb/feb20tojune20.csv')