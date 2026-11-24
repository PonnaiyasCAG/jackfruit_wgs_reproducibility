#!/usr/bin/env python3
"""
Figure 11: Comparative KEGG Metabolic Pathway Landscape Across Jackfruit Cultivars
Reproduces the top 20 KEGG biological pathways compared across:
Indian PLJS, Chinese S10, and Bangladesh BSMRAU-JF-1.
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif', 'serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9.5,
    'figure.titlesize': 13,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../data"))
FIG_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../figures"))
os.makedirs(FIG_DIR, exist_ok=True)

COLOR_PLJS   = "#1f77b4" # Royal Blue
COLOR_S10    = "#d62728" # Crimson Red
COLOR_BSMRAU = "#2ca02c" # Forest Green

def plot_fig11():
    print("Generating Figure 11: Comparative KEGG Pathway Landscape...")
    df_kegg = pd.read_csv(os.path.join(DATA_DIR, "comparative_top_KEGG_pathways.tsv"), sep="\t")
    
    # Exclude global 'Metabolic pathways' for finer pathway resolution
    df_filtered = df_kegg[df_kegg['Pathway_ID'] != 'ko01100'].head(18).copy()
    df_filtered['Short_Name'] = df_filtered['Pathway_Name'].apply(lambda x: x[:36] + '...' if len(x) > 38 else x)
    df_sorted = df_filtered.iloc[::-1]
    
    fig, ax = plt.subplots(figsize=(12, 8.5))
    
    y_pos = np.arange(len(df_sorted))
    bar_height = 0.26
    
    ax.barh(y_pos + bar_height, df_sorted['Indian_PLJS_Genes'], height=bar_height, label='Indian PLJS', color=COLOR_PLJS, alpha=0.9, edgecolor='black', linewidth=0.5)
    ax.barh(y_pos, df_sorted['Chinese_S10_Genes'], height=bar_height, label='Chinese S10', color=COLOR_S10, alpha=0.9, edgecolor='black', linewidth=0.5)
    ax.barh(y_pos - bar_height, df_sorted['BSMRAU_JF1_Genes'], height=bar_height, label='BSMRAU-JF-1', color=COLOR_BSMRAU, alpha=0.9, edgecolor='black', linewidth=0.5)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df_sorted['Short_Name'], fontsize=10)
    ax.set_xlabel("Annotated Gene Count", fontweight='bold', fontsize=11)
    ax.set_title("Top Conserved and Differential KEGG Biological Pathways Across Three Jackfruit Cultivars", fontweight='bold', pad=15, fontsize=12)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc', fontsize=10.5)
    
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig11_comparative_kegg_pathway_landscape.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 11: {fout}")

if __name__ == "__main__":
    plot_fig11()
