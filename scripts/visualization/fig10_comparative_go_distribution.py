#!/usr/bin/env python3
"""
Figure 10: Three-Way Comparative Gene Ontology (GO) Distribution across Jackfruit Cultivars
Reproduces the 3-panel comparative landscape of top Biological Process (BP),
Molecular Function (MF), and Cellular Component (CC) terms across:
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

def plot_fig10():
    print("Generating Figure 10: Comparative GO Functional Distribution...")
    df_bp = pd.read_csv(os.path.join(DATA_DIR, "comparative_top_GO_BP.tsv"), sep="\t")
    df_mf = pd.read_csv(os.path.join(DATA_DIR, "comparative_top_GO_MF.tsv"), sep="\t")
    df_cc = pd.read_csv(os.path.join(DATA_DIR, "comparative_top_GO_CC.tsv"), sep="\t")
    
    def clean_go(df):
        df_clean = df[~df['GO_ID'].isin(['GO:0008150', 'GO:0003674', 'GO:0005575'])].copy()
        df_clean['Clean_Name'] = df_clean['GO_Name'].str.replace("obsolete ", "").str.capitalize()
        df_clean['Clean_Name'] = df_clean['Clean_Name'].apply(lambda x: x[:36] + '...' if len(x) > 38 else x)
        return df_clean.head(10)
    
    top_bp = clean_go(df_bp)
    top_mf = clean_go(df_mf)
    top_cc = clean_go(df_cc)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 7.5), sharey=False)
    
    categories = [
        ('Biological Process (BP)', top_bp, axes[0]),
        ('Molecular Function (MF)', top_mf, axes[1]),
        ('Cellular Component (CC)', top_cc, axes[2])
    ]
    
    bar_height = 0.25
    
    for title, df, ax in categories:
        df_sorted = df.iloc[::-1]
        y_pos = np.arange(len(df_sorted))
        
        ax.barh(y_pos + bar_height, df_sorted['Indian_PLJS_Genes'], height=bar_height, label='Indian PLJS', color=COLOR_PLJS, alpha=0.9, edgecolor='black', linewidth=0.5)
        ax.barh(y_pos, df_sorted['Chinese_S10_Genes'], height=bar_height, label='Chinese S10', color=COLOR_S10, alpha=0.9, edgecolor='black', linewidth=0.5)
        ax.barh(y_pos - bar_height, df_sorted['BSMRAU_JF1_Genes'], height=bar_height, label='BSMRAU-JF-1', color=COLOR_BSMRAU, alpha=0.9, edgecolor='black', linewidth=0.5)
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df_sorted['Clean_Name'], fontsize=9.5)
        ax.set_xlabel("Annotated Gene Count", fontweight='bold')
        ax.set_title(title, fontweight='bold', pad=10, fontsize=11.5)
        ax.grid(axis='x', linestyle='--', alpha=0.4)
        ax.set_axisbelow(True)
        
        if ax == axes[0]:
            ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')
            
    fig.suptitle("Three-Way Comparative Gene Ontology (GO) Distribution across Jackfruit Cultivars", fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    fout = os.path.join(FIG_DIR, "fig10_comparative_go_functional_distribution.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 10: {fout}")

if __name__ == "__main__":
    plot_fig10()
