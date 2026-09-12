import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    # Категории когнитивных функций
    categories = ['Когнитивная гибкость', 'Рабочая память', 
                  'Концентрация внимания', 'Тормозной контроль', 
                  'Аналитическое мышление']
    N = len(categories)

    # Условные баллы для двух групп (от 0 до 100)
    healthy_norm = [85, 82, 88, 78, 80]
    sva_group = [42, 55, 38, 45, 50]

    # Для лепестковой диаграммы нужно "замкнуть" круг, добавив первое значение в конец
    healthy_norm += healthy_norm[:1]
    sva_group += sva_group[:1]

    # Расчет углов для каждой оси (тоже замыкаем)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # Создаем холст с полярными осями
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

    # Настройка осей и подписей
    plt.xticks(angles[:-1], categories, color='black', size=10)
    ax.set_rlabel_position(30) # Сдвигаем шкалу с цифрами, чтобы она не сливалась с осью
    plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"], color="grey", size=8)
    plt.ylim(0, 100)

    # Рисуем зону "Здоровая норма"
    ax.plot(angles, healthy_norm, linewidth=2.5, linestyle='solid', label='Здоровая норма', color='#2ecc71')
    ax.fill(angles, healthy_norm, '#2ecc71', alpha=0.15)

    # Рисуем зону "Зависимость (SVA)"
    ax.plot(angles, sva_group, linewidth=2.5, linestyle='solid', label='Зависимость от коротких видео', color='#e74c3c')
    ax.fill(angles, sva_group, '#e74c3c', alpha=0.25)

    # Добавляем заголовок
    plt.title('Разрушение когнитивной гибкости при SVA', size=13, fontweight='bold', pad=35)

    # --- ИСПРАВЛЕНИЕ НАЛОЖЕНИЯ ---
    # loc='upper center' и bbox_to_anchor сдвигают легенду вниз, под сам график
    # ncol=2 выстраивает легенду в одну красивую строку (по два элемента)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

    plt.tight_layout()
    
    output_path = os.path.join("static", "images", "sva_cognitive_radar.png")
    
    # ИСПРАВЛЕНИЕ: bbox_inches='tight' не даст обрезать сдвинутую вниз легенду при сохранении
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
