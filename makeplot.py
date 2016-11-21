import numpy as np
import matplotlib.pyplot as plt

y = [ 55, 52, 40, 44, 41]

plt.title("Count of top 20 words in sample of tweets")
plt.xticks(('The', 'Quick', 'Brown', 'Fox', 'Jumps'))
plt.bar(x,y, align = 'center')
plt.show()
