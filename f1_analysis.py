import matplotlib.pyplot as plt
import numpy as np
games = [1,2,3,4,5]

ferrari_points = [10,5,4,15,20]
mercedes_points = [15,11,14,5,7]
williams_points = [5,6,9,10,5]
redbull_points = [20,22,11,10,5]
mclaren_points = [25,20,15,19,29]

plt.figure()
plt.title("Scores of past 5 Games in F1")
plt.xlabel("Past 5 Races")
plt.ylabel("Team Scores")

plt.plot(games, ferrari_points, color="r", linestyle="-", label="Ferrari")
plt.plot(games, mercedes_points, color="k", linestyle="--", label="Mercedes")
plt.plot(games, williams_points, color="b", linestyle="-.", label="Williams")
plt.plot(games, redbull_points, color="m", linestyle=":", label="Redbull")
plt.plot(games, mclaren_points, color="y", linestyle="--", label="McLaren")

plt.legend()
plt.show()
