from classes import *
import os
from pathlib import Path

# Define the new base directory path
base_path = Path(r'C:\Users\PA_Mdorio\Northwell Health\CBO DPU Leadership - Dashboard Files\Dashboard Files\Master Data Directory\Peconic')

def test_A2AINP_files():
    files = list((base_path / 'A2PINP').glob('*$$A2AINP.rtf'))
    for file_path in files:
        df = A2AINP(file_path).convert_to_dataframe()
        assert df.shape == (31, 5)
        print(f"Processed {file_path}, shape: {df.shape}")

def test_A2AOUT2_files():
    files = list((base_path / 'A2OUT2').glob('*$$A2OUT2.rtf'))
    for file_path in files:
        df = A2AOUT2(file_path).convert_to_dataframe()
        assert df.shape == (504, 5)
        print(f"Processed {file_path}, shape: {df.shape}")

def test_A2PAMB_files():
    files = list((base_path / 'A2PAMB').glob('*$$A2PAMB.rtf'))
    for file_path in files:
        df = A2PAMB(file_path).convert_to_dataframe()
        assert df.shape == (312, 5)
        print(f"Processed {file_path}, shape: {df.shape}")

def test_A2OSUR_files():
    files = list((base_path / 'A2OSUR').glob('*$$A2OSUR.rtf'))
    for file_path in files:
        df = A2OSUR(file_path).convert_to_dataframe()
        assert df.shape == (4, 5)
        print(f"Processed {file_path}, shape: {df.shape}")