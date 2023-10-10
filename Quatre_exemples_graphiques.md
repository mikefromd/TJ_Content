# Four examples using TigerJython's gturtle library 

## Spiralling Squares

```Python
from gturtle import *

makeTurtle()
size = 1

while True:
    forward(size)
    right(91)
    size += 1
```

![gturtle example 1](Media/231010_gturtle_ex1.png)