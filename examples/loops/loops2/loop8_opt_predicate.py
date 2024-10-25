
from unittest.mock import MagicMock

globals = MagicMock()

segments = ["Segment {}".format(i) for i in range(50000 * 500)]
self = MagicMock()
last_word = MagicMock()
results = []
enumerate = MagicMock()

self.decimals = ['0.5', '1.5', '2.5']
self.multipliers = ['two', 'three']

print("Loop is starting...") 
for i, segment in enumerate(segments):
    stripped_segment = segment.strip()
    if not stripped_segment:
        continue 

    results.append(segment)
    
    if i < len(segments) - 1:
        last_word = segment.rsplit(maxsplit=2)[-1]  
        if last_word in self.decimals or last_word in self.multipliers:
            results.append('point five')
        else:
            results.append('and a half')


print("Loop has finished.")  
