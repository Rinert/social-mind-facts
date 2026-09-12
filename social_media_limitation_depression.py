import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    # Создаем папку static/images, если ее еще нет
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    metrics = ['Депрессия', 'Одиночество', 'Тревожность', 'FOMO']
    control_group = [14.5, 18.2, 16.0, 21.3]  # Контрольная группа (без ограничений)
    limited_group = [8.1, 11.4, 12.8, 14.2]   # Группа с лимитом 30 мин/день

    x = np.arange(len(metrics))  # Позиции категорий по оси X
    width = 0.35                 # Ширина одного столбца

    # plt.subplots() создает холст (fig) и сетку осей (ax)
    fig, ax = plt.subplots(figsize=(8, 5))

    # ax.bar() рисует параллельные столбцы для двух групп
    rects1 = ax.bar(x - width/2, control_group, width, label='Контрольная группа (без лимита)', color='#e74c3c')
    rects2 = ax.bar(x + width/2, limited_group, width, label='Лимит 30 мин/день', color='#2ecc71')

    # Настройка подписей осей, заголовка и легенды
    ax.set_ylabel('Баллы по клиническим шкалам')
    ax.set_title('Снижение психологического неблагополучия через 3 недели', fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()  # Отображает блок с цветовыми метками

    plt.tight_layout()  # Подгоняет размер полей, чтобы весь текст поместился
    
    output_path = os.path.join("static", "images", "social_media_limitation_depression.png")
    plt.savefig(output_path, dpi=300)  # Сохранение графика в высоком качестве
    plt.close()                        # Освобождение оперативной памяти
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
