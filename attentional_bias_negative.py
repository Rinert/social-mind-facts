import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    groups = ['Здоровая норма', 'Зависимость от коротких видео (SVA)']
    positive_dwell = [62, 28]  # Процент времени фиксации взгляда на позитивных стимулах
    negative_dwell = [38, 72]  # Процент времени фиксации взгляда на негативных стимулах

    x = np.arange(len(groups))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(x - width/2, positive_dwell, width, label='Позитивные / нейтральные стимулы', color='#2ecc71')
    ax.bar(x + width/2, negative_dwell, width, label='Негативные / тревожные стимулы', color='#c0392b')

    # Добавление точности данных над столбцами через ax.annotate
    for i in range(len(groups)):
        ax.annotate(f'{positive_dwell[i]}%', (x[i] - width/2, positive_dwell[i] + 1.5), ha='center', fontweight='bold')
        ax.annotate(f'{negative_dwell[i]}%', (x[i] + width/2, negative_dwell[i] + 1.5), ha='center', fontweight='bold')

    ax.set_ylabel('Время фиксации взгляда (%)')
    ax.set_title('Искажение внимания к негативным стимулам (Айтрекинг)', fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_ylim(0, 85)
    ax.legend()

    plt.tight_layout()
    output_path = os.path.join("static", "images", "attentional_bias_negative.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
