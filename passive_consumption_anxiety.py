import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    indicators = ['Социальный капитал', 'Удовлетворенность жизнью', 'Чувство отчуждения', 'Социальная тревожность']
    active_usage = [2.4, 1.9, -1.2, -1.5]   # Влияние активного взаимодействия (комментарии, контент)
    passive_usage = [-1.8, -2.1, 2.6, 2.3]  # Влияние пассивного скроллинга

    y = np.arange(len(indicators))  # Позиции по вертикальной оси Y
    height = 0.35                   # Высота полосы

    fig, ax = plt.subplots(figsize=(10, 6))

    # ax.barh() создает горизонтальные полосы вместо вертикальных столбцов
    ax.barh(y - height/2, active_usage, height, label='Активное участие', color='#3498db')
    ax.barh(y + height/2, passive_usage, height, label='Пассивный скроллинг', color='#e67e22')

    ax.set_xlabel('Индекс влияния', fontsize=11)
    ax.set_title('Разница воздействия активного и пассивного контента', fontsize=12, fontweight='bold', pad=15)
    ax.set_yticks(y)
    ax.set_yticklabels(indicators, fontsize=10)
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Разделительная нулевая линия
    ax.legend(loc='lower right', fontsize=9)

    # Добавление значений на полосы
    for i, (a, p) in enumerate(zip(active_usage, passive_usage)):
        ax.text(a, y[i] - height/2, f'{a}', va='center', ha='right' if a < 0 else 'left', fontsize=8)
        ax.text(p, y[i] + height/2, f'{p}', va='center', ha='right' if p < 0 else 'left', fontsize=8)

    plt.tight_layout()
    output_path = os.path.join("static", "images", "passive_consumption_anxiety.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()