from datetime import datetime

class BonusCalculator:
    def __init__(self, rules):
        self.rules = rules

    def is_holiday(self, timestamp):
        # Простая реализация для выходных дней
        return timestamp.weekday() >= 5

    def calculate(self, amount, timestamp, customer_status):
        applied_rules = []
        total_bonus = 0

        # Базовое правило: 1 бонус за каждые $10
        base_bonus = amount // self.rules['base_rules'][0]['rate']
        total_bonus = base_bonus
        applied_rules.append({
            'rule': self.rules['base_rules'][0]['name'],
            'bonus': base_bonus
        })

        # Правила для выходных/праздников
        for holiday_rule in self.rules['holiday_rules']:
            if holiday_rule['condition'] == 'is_holiday' and self.is_holiday(timestamp):
                total_bonus *= holiday_rule['rate']
                applied_rules.append({
                    'rule': holiday_rule['name'],
                    'bonus': total_bonus - base_bonus
                })

        # Правила для статуса клиента
        for status_rule in self.rules['status_rules']:
            if (status_rule['condition'] == 'is_vip' and 
                customer_status.lower() == 'vip'):
                increase = total_bonus * status_rule['rate']
                total_bonus += increase
                applied_rules.append({
                    'rule': status_rule['name'],
                    'bonus': increase
                })

        return {
            'total_bonus': round(total_bonus, 2),
            'applied_rules': applied_rules
        }
