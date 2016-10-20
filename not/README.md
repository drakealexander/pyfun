# [⏪ When Not to Pick Python](/README.md)

Like any technology Python has its sweet spots and square peg
challenges. The [sweet spots](/why/README.md) convince many to use
Python but let's talk about the square pegs for a bit.

## [⏫ Concurrency](#)

Python shows its age a bit on this front. While there are a lot of add
ons good concurrency is not fundamentally built into the language.
’Dems fightin’ words to a lot of Python supports but it is simply
true. JavaScript gets around this in its own asynchronous way, which
can be added onto Python as well. Go has perhaps one of the best
concurrency models that is abstracted from the underlying operating
system.

## [⏫ Not a Web Language](#)

Python can run in the web browser thanks to many remarkable JavaScript
implementations of Python interpreters but at its heart is not a
web language. This does not mean it is not used for the web, only
that running Python in a web browser directly is impossible. Python
has been one of the main server-side languages, however, even though
it is losing ground to Node and Go as the
[JAMStack.org](http://jamstack.org) model becomes more mainstream.

## [⏫ Slow](#)

Python is slow by design, it is interpreted. Slow is obviously
relative but when compared to raw compiled C or Go or Java code is
falls pretty short unless the slow parts have been written as C/C++
modules, which are pretty easy to add if you need them. Most will
never be affected by this, but this makes Python the lesser choice for
creating server-side web services, (which the compiled Go is really
dominating at the moment even compared to Node). Some would argue that
for web services the lost speed is negligible once the program is
running since the biggest hit is in the startup, but speed comparisons
still show dramatic differences, differences that have caught the
attention of many in the industry.

## [⏫ No Python IDLE?](#)

We cover a lot of concepts in this course, much more than most
textbooks would but you are learning it correctly, the way most
professionals use Python, not the way many traditional educators
and books would have you learn it, unfortunately. Many would have
you play around with Python IDLE, Charm, Sublime, Atom, Eclipse or
some other mousy text editor. While these are better than nothing
you really need to learn to create Python code with nothing but a
command line since very often you will be remotely connecting to a
Linux/UNIX server (as we have) to do something and being able to
be productive quickly, which is what Python is all about, will make
all the difference professionally.

> 💬 Using Python graphically is more popular these days for data
> science visualization and crunching, but web technology dominates
> data visualization currently—especially with [D3](http://d3js.org). By
> Python’s own mantra, “there is one best way to do something” you
> should stick with Python on the command line crunching data, testing
> things, linking them together and the rest of Python’s core
> strengths and focus on web technology 
> for any kind of graphic user experience.

Take the extra time to learn Python right.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

