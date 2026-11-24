#!/usr/bin/env python3
"""
Figure 7: Inferred Moraceae Phylogenomic Species Tree & Evolutionary Radiation
Visualizes the 5-taxa Moraceae tree based on 5,590 single-copy orthologues, with divergence
time estimates (70 Mya Moraceae crown, 45 Mya Artocarpeae, 12 Mya A. heterophyllus)
and dedicated enclosure of the three Asian jackfruit cultivars (PLJS, S10, BSMRAU-JF-1).
"""
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
FIG_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../figures"))
os.makedirs(FIG_DIR, exist_ok=True)

def plot_fig7():
    print("Generating Figure 7: Moraceae Phylogenomic Species Tree...")
    fig, ax = plt.subplots(figsize=(15.5, 8.2))
    
    leaves = [
        {"name": "Indian PLJS (Tamil Nadu, South India)", "variety": "PLJS (Target Indian Landrace)", "genome": "880.18 Mb (28 Chr)", "ploidy": "2n = 4x = 56", "color": "#1F4E79", "y": 5.1},
        {"name": "BARI Kanthal / BSMRAU-JF-1 (Gazipur, Bangladesh)", "variety": "BARI Kanthal (South Asian Cultivar)", "genome": "839.22 Mb (28 Chr)", "ploidy": "2n = 4x = 56", "color": "#2E7D32", "y": 4.1},
        {"name": "Chinese S10 (Guangxi, China)", "variety": "S10 (East Asian Reference)", "genome": "985.63 Mb (28 Chr)", "ploidy": "2n = 4x = 56", "color": "#8C6D31", "y": 3.1},
        {"name": "Morus alba (White Mulberry)", "variety": "Sister Moraceae Lineage", "genome": "330.00 Mb (14 Chr)", "ploidy": "2n = 28", "color": "#E67E22", "y": 1.9},
        {"name": "Ficus carica (Common Fig)", "variety": "Outgroup Root", "genome": "356.00 Mb (13 Chr)", "ploidy": "2n = 26", "color": "#C0392B", "y": 0.9}
    ]
    
    # Draw branches
    # Root to Ficus
    ax.plot([0, 1.5, 1.5, 7.0], [3.0, 3.0, 0.9, 0.9], color='#222222', lw=2.2)
    # Root to Morus/Artocarpus node
    ax.plot([1.5, 3.2], [3.0, 3.0], color='#222222', lw=2.2)
    # Morus branch
    ax.plot([3.2, 3.2, 7.0], [3.0, 1.9, 1.9], color='#222222', lw=2.2)
    # Node to Artocarpus clade
    ax.plot([3.2, 4.8], [3.0, 4.1], color='#222222', lw=2.2)
    # Artocarpus clade to Chinese S10
    ax.plot([4.8, 5.8, 5.8, 7.0], [4.1, 4.1, 3.1, 3.1], color='#222222', lw=2.2)
    # South Asian Ancestor to Bangladesh / PLJS
    ax.plot([5.8, 6.4], [4.1, 4.6], color='#222222', lw=2.2)
    # Bangladesh BARI Kanthal branch
    ax.plot([6.4, 6.4, 7.0], [4.6, 4.1, 4.1], color='#222222', lw=2.2)
    # Indian PLJS branch
    ax.plot([6.4, 6.4, 7.0], [4.6, 5.1, 5.1], color='#222222', lw=2.2)
    
    # Bootstrap nodes
    nodes = [(1.5, 3.0, "100"), (3.2, 3.0, "100"), (4.8, 4.1, "100"), (5.8, 4.1, "99"), (6.4, 4.6, "98")]
    for nx, ny, bs in nodes:
        ax.scatter(nx, ny, s=65, color='#1F4E79', zorder=6, edgecolors='white', linewidth=1.2)
        ax.text(nx - 0.22, ny + 0.16, f'{bs}%', fontsize=8.5, fontweight='bold', color='#1F4E79')

    # Draw Taxa Leaf Badges and Labels
    for leaf in leaves:
        ly = leaf["y"]
        ax.scatter(7.0, ly, s=90, color=leaf["color"], zorder=6, edgecolors='black', linewidth=1.2)
        ax.text(7.25, ly + 0.10, leaf["name"], fontsize=11, fontweight='bold', color='#111111')
        ax.text(7.25, ly - 0.20, f'• Variety: {leaf["variety"]}   |   Assembly: {leaf["genome"]}   |   Ploidy: {leaf["ploidy"]}',
                fontsize=9.3, color='#444444', fontstyle='italic')

    # Artocarpus heterophyllus Clade Box
    rect = patches.Rectangle((4.6, 2.5), 10.4, 3.3, linewidth=1.4, edgecolor='#1F4E79', facecolor='#EBF5FB', alpha=0.45, linestyle='--')
    ax.add_patch(rect)
    ax.text(4.75, 5.58, 'Artocarpus heterophyllus Clade (3 Asian Varieties: PLJS, S10, BARI Kanthal; 2n = 4x = 56, 28 Chromosomes)',
            fontsize=10.5, fontweight='bold', color='#1F4E79')

    # Time Scale (Mya)
    ax.plot([1.0, 7.0], [0.2, 0.2], color='#333333', lw=1.5)
    for tx, label in [(1.0, "70 Mya\n(Moraceae Crown)"), (3.2, "45 Mya\n(Artocarpeae Divergence)"), (4.8, "12 Mya\n(A. heterophyllus)"), (6.4, "< 1.5 Mya\n(South Asian Diversification)"), (7.0, "Present")]:
        ax.plot([tx, tx], [0.12, 0.28], color='#333333', lw=1.2)
        ax.text(tx, -0.08, label, ha='center', va='top', fontsize=8.8, fontweight='bold', color='#333333')

    ax.set_xlim(-0.5, 15.6)
    ax.set_ylim(-0.4, 6.0)
    ax.axis('off')
    ax.set_title('Inferred Moraceae Phylogenomic Species Tree & Evolutionary Radiation of 3 Jackfruit Varieties\n(PLJS, S10, and BARI Kanthal / BSMRAU-JF-1; 5,590 Single-Copy Orthologues via OrthoFinder & STRIDE)',
                 fontsize=13, fontweight='bold', pad=18)

    plt.tight_layout()
    fout = os.path.join(FIG_DIR, "fig7_moraceae_phylogenomic_tree.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 7: {fout}")

if __name__ == "__main__":
    plot_fig7()
