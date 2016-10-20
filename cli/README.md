# [⏪ The Python Command Interface](/README.md)

This lesson focuses on the `python3` command itself and how to use it
to run Python code from the built in command interface and why you
might do such a thing.

## [⏫ Why CLI?](#)

> Concepts: `python3`

The command interface is great for testing a bit of Python before
adding it to your code. 

> 🍎 The CLI is also really good to demonstrated a concept quickly
> so you will see it a lot in instructional material.

One good example is showing how the *join operator* works differently
when applied to numbers and strings.

![](/assets/allowance.gif)

## [⏫ Easter Eggs](#)

> Concepts: Easter Eggs, Zen of Python, Python Longevity

There are a few fun ***Easter eggs*** you can run from the CLI.

> 👓 An *Easter egg* in this sense is some little bit of code not
> documented that the developer left in for whatever reason, sometimes
> to have a little fun. Be careful, though, when considering putting
> them in your own code you are writing for others. More than one
> career has been destroyed over a simple unauthorized *Easter egg*
> some unlucky developer thought would be fun.

### [⏫ The Zen of Python: `import this`](#)

This one is actually part of the Python specification as [PEP-20][]
and a core part of the approach of the language. 

[PEP-20]: https://www.python.org/dev/peps/pep-0020/

![](/assets/import-this.gif)

> 💬 Many would say it is because of *Zen of Python* that it beat
> Perl and remains a valid competitor to many well established
> enterprise languages such as Java and remains the darling of 
> successful software development behemoths like Google and IBM.

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### [⏫ `from __future__ import braces`](#)

This is one not a lot of veteran Python developers even know about.
There have been other April Fool’s day jokes but this one seems to
have stuck.

![](/assets/future-braces.gif)

```
>>> from __future__ import braces
  File "<stdin>", line 1
  SyntaxError: not a chance
```

## [⏫ Conclusion](#)

Use the command interface when you need to test something quickly or
demonstrate a concept. Beyond that use a script.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

