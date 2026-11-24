#!/usr/bin/env python3
"""
Figure 5: Three-Way Cultivar Assembly & Cross-Species Mapping Rate Comparison
Compares assembly contiguity (N50, total length, scaffold count) across Indian PLJS,
Chinese S10, and Bangladesh BSMRAU-JF-1, along with cross-species read mapping rates.
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

def plot_fig5():
    print("Generating Figure 5: Assembly & Mapping Comparisons...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.2))
    
    # Left Panel: Assembly Metrics across 3 Cultivars
    cultivars = ['Indian PLJS\n(Chromosome-Scaffolded)', 'Chinese S10\n(Chromosome Reference)', 'BSMRAU-JF-1\n(Scaffold-level)']
    lengths_mb = [880.18, 985.63, 839.22]
    colors_cult = ['#1F4E79', '#8C6D31', '#2E7D32']
    
    x = np.arange(len(cultivars))
    bars = ax1.bar(x, lengths_mb, color=colors_cult, width=0.45, edgecolor='#111111', linewidth=1.1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(cultivars, fontweight='bold', fontsize=10)
    ax1.set_ylabel('Total Genome Assembly Span (Mb)', fontweight='bold')
    ax1.set_title('A. Total Genome Span across Three Asian Jackfruit Cultivars\n(Indian PLJS: 880.18 Mb; Chinese S10: 985.63 Mb; BSMRAU-JF-1: 839.22 Mb)', fontweight='bold', pad=15)
    ax1.set_ylim(0, 1150)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    for bar in bars:
        h = bar.get_height()
        ax1.annotate(f'{h:.2f} Mb', xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 6),
                     textcoords="offset points", ha='center', fontsize=9.5, fontweight='bold')
        
    # Right Panel: Cross-Species Read Mapping Rates
    species_wrapped = [
        'Jackfruit (A. heterophyllus)\n[Intraspecific PLJS Reads]',
        'White Mulberry (Morus alba)\n[Moraceae; ~45 Myr diverged]',
        'Common Fig (Ficus carica)\n[Moraceae Outgroup; ~70 Myr diverged]'
    ]
    mapped_pct = [99.45, 27.49, 11.08]
    unmapped_pct = [0.55, 72.51, 88.92]
    colors_mapped = ['#1E73BE', '#E67E22', '#C0392B']
    
    y = np.arange(len(species_wrapped))
    height = 0.42
    
    ax2.barh(y, mapped_pct, color=colors_mapped, height=height, edgecolor='#111111', linewidth=1.1, label='Mapped Reads (%)')
    ax2.barh(y, unmapped_pct, left=mapped_pct, color='#EAECEE', height=height, edgecolor='#111111', linewidth=0.8, label='Unmapped Reads (%)')
    
    for i, (m, u) in enumerate(zip(mapped_pct, unmapped_pct)):
        if m > 30:
            ax2.text(m / 2, i, f'{m:.2f}% Mapped', ha='center', va='center', fontsize=9.5, fontweight='bold', color='white')
        else:
            ax2.text(m + 4, i, f'{m:.2f}% Mapped', ha='left', va='center', fontsize=9.5, fontweight='bold', color='#111111')
        ax2.text(mapped_pct[i] + u / 2, i, f'{u:.2f}% Unmapped', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#555555')
    
    ax2.set_yticks(y)
    ax2.set_yticklabels(species_wrapped, fontsize=10, fontweight='bold')
    ax2.invert_yaxis()
    ax2.set_xlim(0, 105)
    ax2.set_xlabel('Read Alignment Rate (%)', fontsize=11, fontweight='bold', labelpad=8)
    ax2.set_title('B. Short-Read DNA Mapping Rates Across Moraceae Taxa\n(Demonstrating Rapid Intraspecific Fidelity vs. Deep Divergence Decay)', fontsize=12, fontweight='bold', pad=48)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.10), ncol=2, frameon=True, facecolor='#ffffff', edgecolor='#cccccc', fontsize=9.5)
    
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig5_assembly_comparison.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 5: {fout}")

if __name__ == "__main__":
    plot_fig5()
