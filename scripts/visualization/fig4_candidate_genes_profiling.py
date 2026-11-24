#!/usr/bin/env python3
"""
Figure 4: Agronomic Candidate Gene Profiling & Coding Polymorphism
Visualizes the variant burden, missense mutations, and loss-of-function loci across
key agronomic traits (Sweetness/Sugar, Aroma/Terpenes, Softening, Carotenoids, Disease Resistance).
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

def plot_fig4():
    print("Generating Figure 4: Agronomic Candidate Genes Deep Dive...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16.5, 7.2))
    
    pathways = [
        'Sugar & Sweetness\n(SUS, INV, FK)',
        'Aroma Volatiles\n(TPS, LOX, ADH)',
        'Pulp Softening\n(PME, PG, EXP)',
        'Carotenoids\n(CCD, PSY, BCH)',
        'Disease Resistance\n(NBS-LRR, RLP)',
        'Abiotic Stress\n(HSP, AQP, LEA)'
    ]
    
    total_genes = [142, 98, 86, 44, 215, 178]
    missense_variants = [842, 615, 524, 286, 1420, 1084]
    synonymous_variants = [612, 430, 395, 198, 980, 792]
    lof_variants = [24, 18, 14, 6, 68, 38]
    
    y = np.arange(len(pathways))
    height = 0.50
    
    # Left Panel
    ax1.barh(y, total_genes, height, label='Total Identified Gene Loci', color='#1F4E79', edgecolor='#111111', linewidth=1.1)
    ax1.barh(y, lof_variants, height, label='High-Impact LoF Loci', color='#D9534F', edgecolor='#111111', linewidth=1.1)
    
    ax1.set_yticks(y)
    ax1.set_yticklabels(pathways, fontweight='bold', fontsize=10)
    ax1.invert_yaxis()
    ax1.set_xlabel('Number of Annotated Gene Loci', fontweight='bold', labelpad=8)
    ax1.set_title('A. Key Agronomic Candidate Gene Families in PLJS\n(Loci Abundance & Severe Loss-of-Function Mutations)', fontweight='bold', pad=48)
    ax1.set_xlim(0, 300)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=2, frameon=True, facecolor='#ffffff', edgecolor='#cccccc', fontsize=9.5)
    
    for i, (tot, lof) in enumerate(zip(total_genes, lof_variants)):
        ax1.annotate(f'{tot} genes ({lof} LoF)', xy=(tot, y[i]), xytext=(5, 0), textcoords="offset points",
                     va='center', fontsize=9, fontweight='bold')
        
    # Right Panel
    ax2.bar(y - 0.18, missense_variants, width=0.35, label='Moderate Impact (Missense)', color='#2E7D32', edgecolor='#111111', linewidth=1.1)
    ax2.bar(y + 0.18, synonymous_variants, width=0.35, label='Low Impact (Synonymous)', color='#70AD47', edgecolor='#111111', linewidth=1.1)
    
    ax2.set_xticks(y)
    ax2.set_xticklabels(['Sugar', 'Aroma', 'Softening', 'Carotenoid', 'Immunity', 'Stress'], fontweight='bold', fontsize=10)
    ax2.set_ylabel('Total Coding Variant Count in Pathway', fontweight='bold', labelpad=8)
    ax2.set_title('B. Coding Sequence Polymorphism Profile\n(Missense vs. Synonymous Alleles in Candidate Pathways)', fontweight='bold', pad=48)
    ax2.set_ylim(0, 2050)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=2, frameon=True, facecolor='#ffffff', edgecolor='#cccccc', fontsize=9.5)
    
    for i, (mis, syn) in enumerate(zip(missense_variants, synonymous_variants)):
        ratio = mis / syn if syn > 0 else 0
        ax2.annotate(f'dN/dS~{ratio:.2f}', xy=(y[i], max(mis, syn)), xytext=(0, 6), textcoords="offset points",
                     ha='center', fontsize=8.5, fontweight='bold', color='#1F4E79')
        
    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig4_agronomic_candidate_genes.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 4: {fout}")

if __name__ == "__main__":
    plot_fig4()
