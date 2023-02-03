times = [['Boston Celtics','Brooklyn Nets','New York Knicks','Philadelphia 76ers','Toronto Raptors','Chicago Bulls','Cleveland Cavaliers','Detroit Pistons','Indiana Pacers','Milwaukee Bucks','Atlanta Hawks','Charlotte Hornets','Miami Heat','Orlando Magic','Washington Wizards'],['Denver Nuggets','Minnesota Timberwolves','Portland Trail Blazers','Oklahoma City Thunder','Utah Jazz','Golden State Warriors','Los Angeles Clippers','Los Angeles Lakers','Phoenix Suns','Sacramento Kings','Dallas Mavericks','Houston Rockets','Memphis Grizzlies','New Orleans Pelicans','San Antonio Spurs']]
CL = times[0]
CO = times[1]
print(times)
cont = 0
for i in range(0, 2):
    for j in times[i]:
        j = str(j)
        print(len(j), cont)
        cont += 1
print(len(CL))
print(len(times[1][1]))
print(times[1][1])