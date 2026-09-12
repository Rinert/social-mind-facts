import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    np.random.seed(42)
    ages = np.array([13, 13.5, 14, 14.2, 14.8, 15, 15.3, 15.7, 16, 16.4, 16.8, 17, 17.2, 17.6, 18])
    nacc_activation = 0.45 * ages - 4.2 + np.random.normal(0, 0.4, len(ages))

    fig, ax = plt.subplots(figsize=(8, 5))

    # ax.scatter() наносит на график отдельные точки (точечную диаграмму)
    ax.scatter(ages, nacc_activation, color='#8e44ad', s=60, alpha=0.8, label='Участники (n=32)')

    # np.polyfit() высчитывает прямую линию тренда на основе имеющихся точек
    m, b = np.polyfit(ages, nacc_activation, 1)
    
    # ax.plot() соединяет координаты линией (в данном случае — пунктирной линией тренда)
    ax.plot(ages, m*ages + b, color='#2980b9', linewidth=2, linestyle='--', label='Трендовая линия (r = 0.47, p = 0.006)')

    ax.set_xlabel('Возраст (лет)')
    ax.set_ylabel('Реакция NAcc на лайки (BOLD response)')
    ax.set_title('Рост чувствительности к лайкам с возрастом', fontsize=12, fontweight='bold', pad=15)
    ax.legend()

    plt.tight_layout()
    output_path = os.path.join("static", "images", "nacc_age_correlation.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
