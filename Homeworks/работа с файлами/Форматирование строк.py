# Использование %
team_1_num = 6
team_2_num = 6
print('в команде "Мастера кода участников": %d' % team_1_num)
print('в команде "Волшебники данных" участников: %d' % team_2_num)
print('Количество участников в обеих командах: %d и %d' %(team_1_num,team_2_num))

# Использовние format()
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('Команда "Волшебники данных" решила {0:d} задач(-и) '.format(score2))
print('Команда "Мастера кода" решила {0:d} задач(-и) '.format(score1))
print('Время за которое команда "Волшебники данных" решила задачи: {0:1.5f} секунд'.format(team2_time))
print('Время за которое команда "Мастера кода" решила задачи: {0:1.3f} секунд'.format(team1_time))


# Использование f-строк
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg_1 = team1_time/score1
time_avg_2= team2_time/score2

print(f'Команды решили: {score1} задач(-и) и {score2} задач(-и)')
print(f'Результат битвы:{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg_1:.3f} секунды на задачу у команды "Мастера кода", и по'
f' по {time_avg_2:.3f} у команды "Волшебники данных"')






