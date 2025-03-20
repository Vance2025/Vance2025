
def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2

skill1_damage, skill2_damage = damage(7,9)
finaldamage = skill1_damage + skill2_damage

print(skill1_damage, skill2_damage)
print('Final Damage is ' + str(finaldamage))





