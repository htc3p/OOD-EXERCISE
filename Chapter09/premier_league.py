'''
สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด
***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***
[ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

ตัวอย่าง
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }
Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68
'''

def selection_sort(teams):
    for i in range(len(teams)-1, 0, -1):
        max_pos = 0
        for j in range(1, i+1):
            if calculate_points(teams[j]) < calculate_points(teams[max_pos]):
                max_pos = j
            if calculate_points(teams[j]) == calculate_points(teams[max_pos]):
                if calculate_gd(teams[j]) < calculate_gd(teams[max_pos]):
                    max_pos = j
        teams[i], teams[max_pos] = teams[max_pos], teams[i]
    
    return teams

def in_to_list(teams):
    results = []
    for team in teams:
        team_name = team['name']
        points = calculate_points(team)
        gd = calculate_gd(team)
        results.append([team_name, {'points': points}, {'gd': gd}])

    return results

def calculate_points(team):
    return int(team['wins']) * 3 + int(team['draws'])

def calculate_gd(team):
    return int(team['scored']) - int(team['conceded'])



teams = input('Enter Input : ').split('/')
teams = [dict(zip(['name', 'wins', 'loss', 'draws', 'scored', 'conceded'], team.split(','))) for team in teams]
results = in_to_list(selection_sort(teams))

print('== results ==')
for result in results:
    print(result)