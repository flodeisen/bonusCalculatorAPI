# Бонусный Калькулятор
Сервис для начисления бонусных баллов пользователям за различные действия в системе

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
    type: multiplier
    condition: always
    rate: 0.1  # 1 бонус за каждые $10

holiday_rules:
  - name: holiday_bonus
    type: multiplier
    condition: is_holiday
    rate: 2.0  # x2 бонусов в выходные/праздники

status_rules:
  - name: vip_boost
    type: percentage_increase
    condition: is_vip
    rate: 0.4  # +40% для VIP-клиентов
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
