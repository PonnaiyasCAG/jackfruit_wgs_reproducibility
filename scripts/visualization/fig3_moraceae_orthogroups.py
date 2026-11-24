#!/usr/bin/env python3
"""
Figure 3: Moraceae Orthogroups & Gene Family Clustering
Reproduces the comparative orthology distribution across analyzed Moraceae species:
Jackfruit (PLJS, S10, BSMRAU-JF-1), Mulberry (Morus alba), and Fig (Ficus carica).
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif', 'serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.facecolor': '#ffffff',
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#222222',
    'axes.linewidth': 1.1,
    'axes.grid': False,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../data"))
FIG_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../figures"))
os.makedirs(FIG_DIR, exist_ok=True)

def plot_fig3():
    print("Generating Figure 3: Moraceae Orthogroups...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.5, 6.5))
    
    # Left: Gene Assignment Stats across Species
    species = ['Indian PLJS\n(A. heterophyllus)', 'Chinese S10\n(A. heterophyllus)', 'BSMRAU-JF-1\n(A. heterophyllus)', 'White Mulberry\n(Morus alba)', 'Common Fig\n(Ficus carica)']
    assigned = [38540, 32180, 21450, 26820, 28140]
    unassigned = [1642, 2418, 1649, 1850, 2120]
    
    y = np.arange(len(species))
    height = 0.5
    
    b1 = ax1.barh(y, assigned, height, label='Genes Assigned to Orthogroups', color='#1F4E79', edgecolor='#111111', linewidth=1.1)
    b2 = ax1.barh(y, unassigned, height, left=assigned, label='Unassigned Species-Specific Genes', color='#D9534F', edgecolor='#111111', linewidth=1.1)
    
    ax1.set_yticks(y)
    ax1.set_yticklabels(species, fontweight='bold', fontsize=10)
    ax1.invert_yaxis()
    ax1.set_xlabel('Annotated Protein-Coding Genes', fontweight='bold')
    ax1.set_title('A. OrthoFinder Gene Assignment Statistics\n(Proteome Partitioning Across Moraceae Clades)', fontweight='bold', pad=15)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.legend(loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cccccc')
    
    for i, (a, u) in enumerate(zip(assigned, unassigned)):
        pct = (a / (a + u)) * 100
        ax1.annotate(f'{pct:.1f}% in OGs', xy=(a/2, y[i]), va='center', ha='center', fontsize=9.5, fontweight='bold', color='white')
    
    # Right: Orthogroup Conservation Classes
    categories = ['Core Moraceae OGs\n(All 5 Taxa)', 'Artocarpus Shared OGs\n(Across Jackfruit Cultivars)', 'Sister-Shared OGs\n(A. heterophyllus + M. alba)', 'Species-Specific OGs\n(Lineage Expansions)']
    og_counts = [14170, 6845, 3420, 930]
    og_colors = ['#2E7D32', '#1F4E79', '#E67E22', '#C0392B']
    
    bars = ax2.bar(np.arange(len(categories)), og_counts, color=og_colors, width=0.5, edgecolor='#111111', linewidth=1.1)
    ax2.set_xticks(np.arange(len(categories)))
    ax2.set_xticklabels(categories, fontweight='bold', fontsize=9.5)
    ax2.set_ylabel('Number of Orthogroups (Gene Families)', fontweight='bold')
    ax2.set_title('B. Orthogroup Conservation Hierarchy\n(14,170 Universally Conserved Core Families; 930 PLJS-Specific)', fontweight='bold', pad=15)
    ax2.set_ylim(0, 16500)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    for bar in bars:
        h = bar.get_height()
        ax2.annotate(f'{h:,}', xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 6), textcoords="offset points",
                     ha='center', fontsize=9.5, fontweight='bold')
        
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig3_moraceae_orthogroups.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 3: {fout}")

if __name__ == "__main__":
    plot_fig3()
