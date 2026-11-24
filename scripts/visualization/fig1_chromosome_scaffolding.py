#!/usr/bin/env python3
"""
Figure 1: Chromosome-Scale Scaffolding of Indian Jackfruit PLJS vs. Chinese S10 Reference
Reproduces the publication-grade bar plot showing placed pseudochromosomes, unplaced scaffolds, and gap junctions.
"""
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Nature/Cell Style Configuration
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif', 'serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
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

def plot_fig1():
    print("Generating Figure 1: Chromosome Scaffolding...")
    fig, ax = plt.subplots(figsize=(9, 5.8))
    categories = ['Chromosome\nPseudochromosomes\n(Placed Span)', 'Unplaced\nScaffolds\n(Unmapped Contigs)', 'Inserted\nN-Gaps\n(Scaffold Junctions)']
    lengths_mb = [751.87, 128.32, 4.50]
    colors = ['#1F4E79', '#D9534F', '#708090']
    
    bars = ax.bar(categories, lengths_mb, color=colors, width=0.45, edgecolor='#111111', linewidth=1.1)
    ax.set_ylabel('Genomic Span (Megabases, Mb)', fontsize=11, fontweight='bold')
    ax.set_title('Chromosome-Scale Scaffolding: Indian PLJS vs. Chinese S10 Reference\n(751.87 Mb / 85.4% Anchored into 28 Pseudochromosomes, 2n = 4x = 56)', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylim(0, 950)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f} Mb\n({(height/880.18)*100:.1f}%)',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#111111')
    
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig1_chromosome_scaffolding.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 1: {fout}")

if __name__ == "__main__":
    plot_fig1()
