import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    systems = ['Система 1\n(Миндалевидное тело / Эмоции)', 'Система 2\n(Префронтальная кора / Контроль)']
    pv_activity = [2.7, -1.9]
    neutral_activity = [0.3, 0.8]

    x = np.arange(len(systems))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(x - width/2, pv_activity, width, label='Алгоритмический контент', color='#e67e22')
    ax.bar(x + width/2, neutral_activity, width, label='Нейтральный контент', color='#7f8c8d')

    ax.set_ylabel('Уровень активации (Z-score)')
    ax.set_title('Подавление когнитивного контроля (Теория двух систем)', fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(systems)
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.legend()

    plt.tight_layout()
    output_path = os.path.join("static", "images", "dual_process_brain.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
