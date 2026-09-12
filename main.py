import vta_dmn_activation
import nacc_age_correlation
import nacc_self_other_usage
import attention_span_decline
import dual_process_brain
import sva_cognitive_radar
import social_media_limitation_depression
import passive_consumption_anxiety
import attentional_bias_negative

def main():
    print("--- Запуск генерации всех 9 графиков ---")
    
    # 1-6. Раздел: Когнитивные функции и внимание
    vta_dmn_activation.generate()
    nacc_age_correlation.generate()
    nacc_self_other_usage.generate()
    attention_span_decline.generate()
    dual_process_brain.generate()
    sva_cognitive_radar.generate()
    
    # 7-9. Раздел: Психоэмоциональное состояние и тревожность
    social_media_limitation_depression.generate()
    passive_consumption_anxiety.generate()
    attentional_bias_negative.generate()
    
    print("--- Генерация успешно завершена! Файлы сохранены в static/images/ ---")

if __name__ == "__main__":
    main()
