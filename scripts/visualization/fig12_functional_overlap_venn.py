#!/usr/bin/env python3
"""
Figure 12: Three-Way Functional Overlap and Conservation (Euler/Venn Diagrams)
Visualizes core conserved vs. cultivar-specific Gene Ontology terms and KEGG pathways
across Indian PLJS, Chinese S10, and Bangladesh BSMRAU-JF-1.
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif', 'serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
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

def plot_fig12():
    print("Generating Figure 12: Functional Overlap Venn Diagrams...")
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    
    def draw_3way_venn(ax, title, counts_dict, total_shared_pct):
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-2.0, 2.2)
        ax.axis('off')
        
        # 3 Circle Centers
        c1 = patches.Circle((-0.55, 0.45), 0.95, alpha=0.35, facecolor=COLOR_PLJS, edgecolor=COLOR_PLJS, lw=2.0)
        c2 = patches.Circle((0.55, 0.45), 0.95, alpha=0.35, facecolor=COLOR_S10, edgecolor=COLOR_S10, lw=2.0)
        c3 = patches.Circle((0.0, -0.45), 0.95, alpha=0.35, facecolor=COLOR_BSMRAU, edgecolor=COLOR_BSMRAU, lw=2.0)
        
        ax.add_patch(c1)
        ax.add_patch(c2)
        ax.add_patch(c3)
        
        # Labels for cultivars
        ax.text(-1.45, 1.25, f"Indian PLJS\n({counts_dict['PLJS_total']:,})", fontsize=11, fontweight='bold', color='#0b406b', ha='center')
        ax.text(1.45, 1.25, f"Chinese S10\n({counts_dict['S10_total']:,})", fontsize=11, fontweight='bold', color='#8a1213', ha='center')
        ax.text(0.0, -1.65, f"BSMRAU-JF-1\n({counts_dict['BSMRAU_total']:,})", fontsize=11, fontweight='bold', color='#145414', ha='center')
        
        # Region counts
        # Core shared center
        ax.text(0.0, 0.12, f"Core Shared\n{counts_dict['Core_3way']:,}\n({total_shared_pct:.1f}%)",
                fontsize=10.5, fontweight='bold', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc', alpha=0.9))
        
        # 2-way intersections
        ax.text(0.0, 0.78, f"{counts_dict['PLJS_S10']:,}", fontsize=9.5, fontweight='bold', ha='center')
        ax.text(-0.55, -0.15, f"{counts_dict['PLJS_BSMRAU']:,}", fontsize=9.5, fontweight='bold', ha='center')
        ax.text(0.55, -0.15, f"{counts_dict['S10_BSMRAU']:,}", fontsize=9.5, fontweight='bold', ha='center')
        
        # Unique regions
        ax.text(-1.10, 0.55, f"{counts_dict['PLJS_only']:,}", fontsize=10, fontweight='bold', ha='center')
        ax.text(1.10, 0.55, f"{counts_dict['S10_only']:,}", fontsize=10, fontweight='bold', ha='center')
        ax.text(0.0, -0.95, f"{counts_dict['BSMRAU_only']:,}", fontsize=10, fontweight='bold', ha='center')
        
        ax.set_title(title, fontweight='bold', fontsize=12, pad=15)
        
    # GO Terms Overlap
    go_counts = {
        'PLJS_total': 11671, 'S10_total': 10582, 'BSMRAU_total': 8652,
        'Core_3way': 10025, 'PLJS_S10': 812, 'PLJS_BSMRAU': 310, 'S10_BSMRAU': 180,
        'PLJS_only': 524, 'S10_only': 165, 'BSMRAU_only': 87
    }
    draw_3way_venn(axes[0], "A. Gene Ontology (GO) Terms Overlap", go_counts, 85.9)
    
    # KEGG Pathways Overlap
    kegg_counts = {
        'PLJS_total': 452, 'S10_total': 449, 'BSMRAU_total': 443,
        'Core_3way': 443, 'PLJS_S10': 5, 'PLJS_BSMRAU': 2, 'S10_BSMRAU': 1,
        'PLJS_only': 2, 'S10_only': 1, 'BSMRAU_only': 0
    }
    draw_3way_venn(axes[1], "B. KEGG Biological Pathways Overlap", kegg_counts, 98.0)
    
    fig.suptitle("Three-Way Functional Overlap and Conservation across Jackfruit Cultivars", fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    fout = os.path.join(FIG_DIR, "fig12_three_jack_functional_overlap_venn.png")
    plt.savefig(fout)
    plt.close()
    print(f"✓ Saved Figure 12: {fout}")

if __name__ == "__main__":
    plot_fig12()
