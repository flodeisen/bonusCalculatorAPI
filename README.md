# Бонусный Калькулятор
## Описание
Сервис для динамического начисления бонусных баллов с гибкой системой правил.

## Требования
- Python 3.9+
- Flask
- PyYAML

## Установка
1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка правил
Правила хранятся в файле `bonus_rules.yaml`. 

Пример конфигурации:
```yaml
base_rules:
  - name: base_rate
    type: divisor
    condition: always
    rate: 10  # 1 бонус за каждые $10
    priority: 1

holiday_rules:
  - name: holiday_bonus
    type: multiplier
    condition: is_holiday
    rate: 2.0  # x2 бонусов в выходные/праздники
    priority: 2

status_rules:
  - name: vip_boost
    type: percentage_increase
    condition: is_vip
    rate: 0.4  # +40% для VIP-клиентов
    priority: 3
```

## Запуск сервиса
```bash
python app.py
```

## Пример использования API
```bash
curl -X POST http://localhost:5000/calculate-bonus \
     -H "Content-Type: application/json" \
     -d '{
         "transaction_amount": 150,
         "timestamp": "2025-03-08T14:30:00Z",
         "customer_status": "vip"
     }'
```

## Структура проекта
- `app.py`: Основной файл приложения с API
- `bonus_rules.yaml`: Конфигурация правил начисления бонусов
- `bonus_calculator.py`: Модуль расчета бонусов
- `requirements.txt`: Зависимости проекта
