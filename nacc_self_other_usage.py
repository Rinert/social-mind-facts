import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    np.random.seed(101)
    delta_nacc = np.linspace(-0.5, 2.5, 25)
    media_usage = 12 + 8.5 * delta_nacc + np.random.normal(0, 2.5, len(delta_nacc))

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(delta_nacc, media_usage, color='#d35400', s=55, alpha=0.85)

    # Построение линии регрессии, показывающей прямую зависимость
    m, b = np.polyfit(delta_nacc, media_usage, 1)
    ax.plot(delta_nacc, m*delta_nacc + b, color='#2c3e50', linewidth=2, label='Прямая регрессии')

    ax.set_xlabel('Дельта активации NAcc (Self > Other)')
    ax.set_ylabel('Использование соцсетей (часов в неделю)')
    ax.set_title('Зависимость активности в соцсетях от реакции мозга на похвалу', fontsize=12, fontweight='bold', pad=15)
    ax.legend()

    plt.tight_layout()
    output_path = os.path.join("static", "images", "nacc_self_other_usage.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
