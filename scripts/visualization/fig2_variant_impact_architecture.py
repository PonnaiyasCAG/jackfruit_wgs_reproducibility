#!/usr/bin/env python3
"""
Figure 2: Variant Impact Architecture & Functional Classification in Jackfruit PLJS
Reproduces the distribution of 17.77M SNPs and InDels across SnpEff impact tiers:
High (LoF), Moderate (Missense), Low (Synonymous), and Modifier (Non-coding/Regulatory).
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

def plot_fig2():
    print("Generating Figure 2: Variant Impact Architecture...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.2))
    
    # Left Panel: All Variants Impact Breakdown (Log/Linear Bar Plot)
    tiers = ['MODIFIER\n(Non-coding / UTRs / Intronic)', 'LOW\n(Synonymous Coding)', 'MODERATE\n(Missense / In-frame)', 'HIGH\n(Loss-of-Function LoF)']
    counts = [17436677, 183210, 142850, 9458]
    colors = ['#808B96', '#27AE60', '#F39C12', '#C0392B']
    
    y = np.arange(len(tiers))
    bars = ax1.barh(y, counts, color=colors, height=0.55, edgecolor='#111111', linewidth=1.1)
    ax1.set_xscale('log')
    ax1.set_yticks(y)
    ax1.set_yticklabels(tiers, fontweight='bold', fontsize=10)
    ax1.invert_yaxis()
    ax1.set_xlabel('Variant Count (Log10 Scale)', fontweight='bold')
    ax1.set_title('A. Whole-Genome SnpEff Impact Distribution\n(17,772,195 Total Evaluated Polymorphisms vs. BSMRAU-JF-1)', fontweight='bold', pad=15)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    for bar in bars:
        w = bar.get_width()
        pct = (w / sum(counts)) * 100
        ax1.annotate(f'{w:,} ({pct:.2f}%)', xy=(w, bar.get_y() + bar.get_height()/2),
                     xytext=(8, 0), textcoords="offset points", va='center', fontsize=9.5, fontweight='bold')
    
    # Right Panel: Coding Polymorphism Breakdown (Pie Chart of Exonic Alterations)
    coding_labels = ['Synonymous (Low)', 'Missense (Moderate)', 'High-Impact LoF']
    coding_counts = [183210, 142850, 9458]
    coding_colors = ['#27AE60', '#F39C12', '#C0392B']
    explode = (0.02, 0.04, 0.08)
    
    wedges, texts, autotexts = ax2.pie(
        coding_counts, labels=coding_labels, autopct='%1.1f%%',
        startangle=140, colors=coding_colors, explode=explode,
        wedgeprops=dict(edgecolor='#111111', linewidth=1.2),
        textprops=dict(fontweight='bold', fontsize=10.5)
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_color('white')
        at.set_fontweight('bold')
    
    ax2.set_title('B. Coding Sequence Mutation Architecture\n(335,518 Exonic Mutations; Missense-to-Synonymous Ratio = 0.78)', fontweight='bold', pad=15)
    
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig2_variant_impact_distribution.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 2: {fout}")

if __name__ == "__main__":
    plot_fig2()
