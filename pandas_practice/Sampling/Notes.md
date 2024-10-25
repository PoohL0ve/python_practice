The population is the complete dataset, it does not necessarily mean the consesus. The sample is a subset of the population.
The **sample(n)** method can return a subset of the population based on the argument value:
```python
import pandas as pd
pots_vs_coffee = pots_vs_coffee.sample(10)  # returns 10 rows
```

A population parameter is a calculation made on the population dataset:
```python
import numpy as np
# french_teams is the population dataset
np.mean(french_teams['nice_teams'])
```

A point estimate or sample statistic is a calculation made on the sample dataset. The pandas statistical methods can also be used like mean().

One way to visualise convenience bias is to plot a histogram:
```python
coffee_sample['total_cups'].hist(bins=np.arange(59, 93, 2))
```

When genrating pseudo-random numbers, the previous number tells the function
what the next numbe will be.
```python
np.random.beta=(a=2, b=2, size=5000)
np.random.seed(20002)
np.random.normal(loc=2, scale=1.5, size=2)

np.random.unifrom(low=-3, high=3, size=4000)
```