import os
import matplotlib.pyplot as plt

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    years = [2004, 2012, 2024]
    attention_span = [150, 75, 47]

    fig, ax = plt.subplots(figsize=(8, 5))

    # параметр marker='o' добавляет видимые узловые точки на изгибах линии
    ax.plot(years, attention_span, marker='o', color='#c0392b', linewidth=2.5, markersize=8)

    # ax.annotate() выводит текст непосредственно поверх указанных точек на графике
    for y, a in zip(years, attention_span):
        ax.annotate(f'{a} сек', (y, a), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

    ax.set_xlabel('Год')
    ax.set_ylabel('Время фокуса на одном экране (секунды)')
    ax.set_title('Деградация устойчивого внимания (2004–2024)', fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(years)
    ax.set_ylim(0, 180)  # Фиксирует нижнюю и верхнюю границы оси Y

    plt.tight_layout()
    output_path = os.path.join("static", "images", "attention_span_decline.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
