import os
import matplotlib.pyplot as plt
import numpy as np

def generate():
    os.makedirs(os.path.join("static", "images"), exist_ok=True)

    categories = ['VTA\n(Дофамин)', 'Amygdala\n(Эмоции)', 'DMN\n(Транс)', 'PFC\n(Контроль)']
    pv_signal = [2.5, 2.1, 2.8, -1.8]
    gv_signal = [0.6, 0.4, 0.7, 0.2]

    x = np.arange(len(categories))  # Массив позиций осей для каждой категории
    width = 0.35                    # Ширина одного столбца

    # plt.subplots() создает "холст" (fig) и область рисования (ax)
    fig, ax = plt.subplots(figsize=(8, 5))

    # ax.bar() рисует столбцы. Смещение (x - width/2) сдвигает их влево/вправо для сравнения
    ax.bar(x - width/2, pv_signal, width, label='Персонализированное видео (PV)', color='#e74c3c')
    ax.bar(x + width/2, gv_signal, width, label='Общее видео (GV)', color='#3498db')

    # Настройка подписей, заголовка и легенды
    ax.set_ylabel('BOLD-сигнал (Z-score)')
    ax.set_title('Реакция зон мозга на персонализированный контент', fontsize=12, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()  # Отображает блок с расшифровкой цветов (легенду)
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Нулевая горизонтальная линия

    plt.tight_layout()  # Автоматически подгоняет поля, чтобы надписи не вылезали за края
    
    output_path = os.path.join("static", "images", "vta_dmn_activation.png")
    plt.savefig(output_path, dpi=300)  # Сохраняет холст в файл картинки
    plt.close()                        # Закрывает графический контекст для освобождения памяти
    print(f"Готово: {output_path}")

if __name__ == "__main__":
    generate()
