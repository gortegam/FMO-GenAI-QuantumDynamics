import matplotlib.pyplot as plt

def plot_populations(tlist, populations, savepath="../results/figures/populations.png"):
    plt.figure(figsize=(8,5))
    for i, pop in enumerate(populations):
        plt.plot(tlist, pop, label=f"Site {i+1}")
    plt.xlabel("Time (ps)")
    plt.ylabel("Excitation Probability")
    plt.title("FMO Complex Site Populations")
    plt.legend()
    plt.tight_layout()
    plt.savefig(savepath)
    plt.close()
