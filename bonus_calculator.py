from datetime import datetime

class BonusCalculator:
    def __init__(self, rules):
        self.rules = rules
        # Сортируем правила при инициализации
        self.sorted_rules = sorted(self.rules['rules'], key=lambda r: r['priority'])

    def is_holiday(self, timestamp):
        return timestamp.weekday() >= 5

    def calculate(self, amount, timestamp, customer_status):
        applied_rules = []
        total_bonus = 0

        for rule in self.sorted_rules:
            if rule['name'] == 'base_rate':
                base_bonus = (amount // rule['divisor']) * rule['bonus']
                total_bonus = base_bonus
                applied_rules.append({
                    'rule': rule['name'],
                    'bonus': base_bonus
                })
            elif rule['name'] == 'holiday_bonus' and rule['condition'].get('is_holiday'):
                if self.is_holiday(timestamp):
                    holiday_bonus = total_bonus * (rule['multiplier'] - 1)
                    total_bonus *= rule['multiplier']
                    applied_rules.append({
                        'rule': rule['name'],
                        'bonus': holiday_bonus
                    })
            elif rule['name'] == 'vip_boost' and rule['condition'].get('is_vip'):
                if customer_status.lower() == 'vip':
                    vip_bonus = total_bonus * (rule['multiplier'] - 1)
                    total_bonus *= rule['multiplier']
                    applied_rules.append({
                        'rule': rule['name'],
                        'bonus': vip_bonus
                    })

        return {
            'total_bonus': round(total_bonus, 2),
            'applied_rules': applied_rules
        }

