#!/usr/bin/env python3
"""
Figure 13: Comparative Gene Counts in Agronomically Important Metabolic Pathways
Reproduces the gene abundance comparison in key agronomic pathways (Starch/Sucrose,
Fructose/Mannose, Glycolysis, Terpenoid backbone, Flavonoids, Phenylpropanoids)
across Indian PLJS, Chinese S10, and Bangladesh BSMRAU-JF-1.
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
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
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

def plot_fig13():
    print("Generating Figure 13: Agronomic Pathway Gene Counts...")
    df = pd.read_csv(os.path.join(DATA_DIR, "comparative_agronomic_KEGG_pathways.tsv"), sep="\t")
    df_sorted = df.iloc[::-1]
    
    fig, ax = plt.subplots(figsize=(12, 7.5))
    y_pos = np.arange(len(df_sorted))
    bar_height = 0.26
    
    rects1 = ax.barh(y_pos + bar_height, df_sorted['Indian_PLJS_Genes'], height=bar_height, label='Indian PLJS', color=COLOR_PLJS, alpha=0.9, edgecolor='black', linewidth=0.5)
    rects2 = ax.barh(y_pos, df_sorted['Chinese_S10_Genes'], height=bar_height, label='Chinese S10', color=COLOR_S10, alpha=0.9, edgecolor='black', linewidth=0.5)
    rects3 = ax.barh(y_pos - bar_height, df_sorted['BSMRAU_JF1_Genes'], height=bar_height, label='BSMRAU-JF-1', color=COLOR_BSMRAU, alpha=0.9, edgecolor='black', linewidth=0.5)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df_sorted['Pathway_Name'], fontsize=10.5, fontweight='bold')
    ax.set_xlabel("Annotated Gene Count", fontweight='bold', fontsize=11)
    ax.set_title("Gene Family Expansion in Key Quality, Flavor, and Secondary Metabolic Pathways", fontweight='bold', pad=15, fontsize=12.5)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')
    
    # Value annotations on bars
    for rects in [rects1, rects2, rects3]:
        for r in rects:
            w = r.get_width()
            ax.annotate(f'{int(w)}', xy=(w, r.get_y() + r.get_height() / 2),
                        xytext=(4, 0), textcoords="offset points", va='center', fontsize=9, fontweight='bold')
            
    ax.set_xlim(0, max(df_sorted['Indian_PLJS_Genes']) * 1.15)
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig13_agronomic_pathway_gene_counts.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 13: {fout}")

if __name__ == "__main__":
    plot_fig13()
