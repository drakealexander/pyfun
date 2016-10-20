# [⏪ Holiday Lights](/README.md)

*Work in progress as we port content into GitHub Classroom*

```python
#!/usr/bin/env python3

import pylights
import colors as c
import time

lights = pylights.Set()
while True:
    lights.color = c.red
    lights.update(0.5)
    lights.color = c.blue
    lights[2].color = c.random()
    lights.update(0.5)
```---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

