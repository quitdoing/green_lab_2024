
from unittest.mock import MagicMock

globals = MagicMock()

segments = ["Segment {}".format(i) for i in range(50000 * 500)]
self = MagicMock()
last_word = MagicMock()
results = []
enumerate = MagicMock()

self.decimals = ['0.5', '1.5', '2.5']
self.multipliers = ['two', 'three']

# Loop execution starts here
print("Loop is starting...") 
for i, segment in enumerate(segments):
    if len(segment.strip()) == 0:
        continue
    if i == len(segments) - 1:
        results.append(segment)
    else:
        results.append(segment)
        last_word = segment.rsplit(maxsplit=2)[-1]
        if last_word in self.decimals or last_word in self.multipliers:
            results.append('point five')
        else:
            results.append('and a half')

print("Loop has finished.")  
