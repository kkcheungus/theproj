import sys
import math

# KK 9/25/2012 add comment

x = []
for line in open(sys.argv[1]):
   num = int(line)
   x.append(num)

avg = sum(x) / float(len(x))

diffs = []
for num in x:
   diff = num - avg
   diffs.append(diff**2)

stddev = math.sqrt(sum(diffs) / float(len(x)))

avg = sum(x) / float(len(x))
sumsqdiffs = sum(diffs) / float(len(x))

print 'the average is', avg, 'and sumsqdiffs is', sumsqdiffs
print 'the stddev is', stddev
