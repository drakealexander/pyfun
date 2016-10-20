# [⏪ Checking the Python Docs](/README.md)

There is simply no way this course can cover everything Python has to
offer. Instead you should get familiar with what every other coder
does to get answers, Google it. Chances are you will mostly get hits
from stackexchange.com. Usually these are very helpful, but sometimes
they are dead wrong or are bad practices. Often solutions in Python2
will be suggested when a better Python3 solution exists. Just be
aware of this.

## [⏫ Make Sure Python3](#)

> Concepts: `docs.python.org`, Standard Documentation, Python Versions

When you go to the standard Python documentation, which can be
a little more difficult to digest sometimes, make sure you update
the version to the version you are using.

![](/assets/docs-version.gif)

## [⏫ Pydoc](#)

> Concepts: `pydoc3`, Comments, `|`, Pagers, Pipes, `| more`,
> `more`, UNIX Pipeline

Sometimes you may not have access to the Internet. Being born
on the command line Python has a built-in documentation system
that does not depend on the web or graphics at all. Type `pydoc3`
to see it.

![](/assets/pydoc.gif)

Notice that the text was too long for the screen. When that happens
you need to pipe the output to a ***pager*** command like `more`. To
do this add a pipe or bar character `|` followed by the command to 
receive the output into its input.

```sh
pydoc3 | more
```

This is a very short ***UNIX pipeline*** and is a fundamental
principle of the UNIX/Linux command line. By chaining together the
output of one command to the input of another you can create very
powerful filters and functionality very quickly.

During this course you will learn how to add comments to your
code in a way that will automatically create documentation using
`pydoc3` for those wanting to read about your code. 

> 💬 We will say this a lot in this course, but it is always good
> to add good documentation to your code for yourself later as
> well as others.

## [⏫ Manual `man` Pages](#)

> Concepts: Man Pages, `man`

![](/assets/man-python3.gif)

Like any other command on Linux/Unix Python also has a `man` page.
The `man` page system predates the Internet as a way to document
commands in a way that can be searched and read from the command
line. Like `pydoc3` this is good when you do not have access to the
Internet.  Man pages are nice because they are automatically paged
for you (no need to pipe the output to `more`).

> 💬 This is probably the best way to remind yourself about all the
> different *environment variables* there are for Python3, like
> `PYTHONPATH`. This course does not cover a lot of the subtle,
> powerful ways to use `python3` directly from the command line
> without writing a script at all. This is also another good place
> to learn about that.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

