#!/usr/bin/env python3
"""
Figure 8: Agronomic Candidate Protein Domain Architecture & Lollipop Mutation Maps
Visualizes functional domain architectures and non-synonymous / missense mutations
for key Jackfruit agronomic candidate genes (Starch Synthetase, Terpene Synthase, Sucrose Synthase, Flavonoid CHS).
Reads structured domain and variant data directly from data/candidate_genes_circos_data.json.
"""
import os
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif', 'serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9,
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

def plot_fig8():
    print("Generating Figure 8: Candidate Protein Domains & Lollipop Mutation Maps...")
    json_path = os.path.join(DATA_DIR, "candidate_genes_circos_data.json")
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
        
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    # Select 4 representative agronomic candidate genes for multi-panel lollipop
    target_symbols = ['SPS', 'TPS_Mono', 'CHS2', 'FUS3_VP1']
    candidates = [c for c in data.get('candidates', []) if c.get('symbol') in target_symbols]
    if not candidates:
        candidates = data.get('candidates', [])[:4]
        
    fig, axes = plt.subplots(len(candidates), 1, figsize=(15, 3.2 * len(candidates)), sharex=False)
    if len(candidates) == 1:
        axes = [axes]
        
    for idx, (ax, cand) in enumerate(zip(axes, candidates)):
        prot_len = cand.get('protein_len_aa', 600)
        symbol = cand.get('symbol', 'Gene')
        name = cand.get('name', '')
        chrom = cand.get('chrom', '')
        trait = cand.get('trait_category', '')
        
        # Backbone (grey bar)
        ax.plot([0, prot_len], [0, 0], color='#BDC3C7', lw=6, solid_capstyle='round', zorder=1)
        
        # Domains
        legend_domains = []
        for d in cand.get('domains', []):
            d_name = d.get('name', 'Domain')
            d_start = d.get('start', 0)
            d_end = d.get('end', prot_len)
            d_color = d.get('color', '#3498DB')
            
            rect = patches.Rectangle((d_start, -0.22), d_end - d_start, 0.44,
                                     facecolor=d_color, edgecolor='#111111', lw=1.1, alpha=0.9, zorder=2)
            ax.add_patch(rect)
            
            # Domain label inside or above
            mid_d = (d_start + d_end) / 2
            ax.text(mid_d, 0, d_name[:24], ha='center', va='center', fontsize=8.5, fontweight='bold', color='white', zorder=3)
            
        # Mutations (Lollipops)
        muts = cand.get('mutations', [])
        # Assign varying heights to avoid overlapping lollipop heads
        for m_idx, m in enumerate(muts):
            pos_aa = m.get('pos_aa', 50)
            m_type = m.get('type', 'Missense')
            m_color = m.get('color', '#E74C3C')
            effect = m.get('effect', '')
            
            h = 0.55 + (m_idx % 3) * 0.28
            # Stick
            ax.plot([pos_aa, pos_aa], [0.22, h], color='#333333', lw=1.2, zorder=4)
            # Head circle
            ax.scatter(pos_aa, h, s=80, facecolor=m_color, edgecolor='#111111', lw=1.1, zorder=5)
            # Mutation text label
            short_eff = effect.split(' - ')[0] if ' - ' in effect else effect
            ax.text(pos_aa, h + 0.08, short_eff, ha='center', va='bottom', fontsize=8, fontweight='bold', rotation=35, color='#222222')
            
        ax.set_xlim(-15, prot_len + 35)
        ax.set_ylim(-0.6, 1.4)
        ax.set_yticks([])
        ax.set_xlabel('Amino Acid Position (aa)', fontweight='bold', fontsize=9.5)
        ax.set_title(f"{symbol} — {name} ({chrom}, {trait}, {prot_len} aa; {len(muts)} Coding Variants in PLJS)",
                     fontweight='bold', fontsize=11, loc='left', pad=10)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
    fig.suptitle('Protein Domain Architecture & Non-Synonymous Lollipop Mutation Landscapes in Curated Agronomic Genes',
                 fontsize=13, fontweight='bold', y=0.99)
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    fout = os.path.join(FIG_DIR, "fig8_candidate_protein_domains_lollipop.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 8: {fout}")

if __name__ == "__main__":
    plot_fig8()
