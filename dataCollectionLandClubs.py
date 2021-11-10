import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
style.use('ggplot')
dic = {'PSG': 530.5, 'Barcelona': 656.8, 'Atletico Madrid': 196.0, 'Man United': 352.6, 'Real Madrid': 634.0, 'Juventus': 337.0, 'Liverpool': 207.0,
       'Inter': 80.0, 'Arsenal': 143.7, 'Chelsea': 286.5, 'Bayern Munich': 80.0, 'Man City': 473.5, 'Napoli': 70.0, 'Shanghai SIPG': 61.0, 'Tottenham': 60.0, 'Monaco': 60.0}

leagues = {'Ligue 1': 590.5, 'Laliga': 1486.8, 'Premier League': 1523.3,
           'Serie A': 487.0, 'Bundesliga': 80.0, 'China': 61.0}

lClubs = {'Ligue 1': ['PSG', 'Monaco'], 'Laliga': ['Barcelona', 'Real Madrid', 'Atletico Madrid'], 'Premier League': ['Man City', 'Man United',
                                                                                                                      'Chelsea', 'Liverpool', 'Arsenal', 'Tottenham'], 'Serie A': ['Juventus', 'Inter', 'Napoli'], 'Bundesliga': ['Bayern Munich'], 'China': ['Shanghai SIPG']}
radius = 10
leagues = dict(sorted(leagues.items(), key=lambda item: item[1], reverse=True))
dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

transfers = [leagues[x] for x in leagues]
clubs = [f"{x}\n€{transfers[index]}m" for index, x in enumerate(leagues)]

fig = plt.figure(figsize=(10, 7))

wedges, text = plt.pie(transfers, labeldistance=1.1, labels=clubs,
                       textprops=dict(
                           va='center', rotation_mode='anchor', ha='center'),
                       startangle=90, radius=10, rotatelabels=True, counterclock=False,
                       wedgeprops={"edgecolor": "white",
                                   'linewidth': 2,
                                   'antialiased': True})

# bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
# kw = dict(arrowprops=dict(arrowstyle="->"),
#           bbox=bbox_props, zorder=0, va="center")
# transfersPct = [t/sum(transfers) for t in transfers]
# for i,p in enumerate(wedges):
#         p.set_radius(radius*transfersPct[i])
#         p.set_radius(p.r+1)
#         ang = (p.theta2 - p.theta1)/2. + p.theta1
#         y = np.sin(np.deg2rad(ang))
#         x = np.cos(np.deg2rad(ang))
#         horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
#         connectionstyle = "angle,angleA=10,angleB={}".format(ang)
#         plt.annotate(clubs[i], xy=(x, y), xytext=(x*(5+(1-transfersPct[i])), y*(5+(1-transfersPct[i]))),
#                 horizontalalignment=horizontalalignment, **kw)

innerClubs = []
innerTransfers = []

for x in leagues:
    for index, club in enumerate(lClubs[x]):
        innerTransfers.append(dic[club])
        if innerTransfers[-1] < 100:
            innerClubs.append(club)
        else:
            innerClubs.append(f"{club}\n€{innerTransfers[-1]}m")

innerWedges, innerText = plt.pie(innerTransfers, labels=innerClubs,
                                 textprops=dict(
                                     va="center", rotation_mode='anchor', ha='center'),
                                 labeldistance=0.6, startangle=90, radius=radius-1,
                                 rotatelabels=True, counterclock=False,
                                 wedgeprops={"edgecolor": "white",
                                             'linewidth': 2,
                                             'antialiased': True})

innerTransfersPct = [t/sum(innerTransfers) for t in innerTransfers]
for i, w in enumerate(innerWedges):
    w.set_radius(3.5+(w.r*2.5*innerTransfersPct[i]))


# circle = plt.Circle((0, 0), 3, fc='white')
# donut = plt.gcf()
# donut.gca().add_artist(circle)
plt.axis('equal')
plt.tight_layout()
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
