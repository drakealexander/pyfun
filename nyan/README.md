# [⏪ Nyan, Nyan, STOP!](/README.md)

## Table of Contents

1. [**Nyan What?**](#user-content--nyan-what)
2. [**The Usual**](#user-content--the-usual)
3. [**True or False**](#user-content--true-or-false)
4. [**Loop It**](#user-content--loop-it)
5. [**In Your Block**](#user-content--in-your-block)
6. [**Indenting with `vim`**](#user-content--indenting-with-vim)
7. [**Spaces and Tabs that Matter**](#user-content--spaces-and-tabs-that-matter)
8. [**Make is STOP!**](#user-content--make-is-stop)
9. [**Catching and Trapping Exceptions**](#user-content--catching-and-trapping-exceptions)
10. [**Printing to Same Line**](#user-content--printing-to-same-line)
 1. [**Flushing**](#user-content--flushing)
11. [**Conclusion**](#user-content--conclusion)
12. [**Bonus Challenges**](#user-content--bonus-challenges)

![](/assets/nyan.gif)

## [⏫ Nyan What?](#)

Unless you have been asleep for the last five years you have probably
heard of the infamous Nyan Cat. If not here is a reminder link to
the YouTube video for your enjoyment.


[![](/assets/nyan-vid.gif)](https://youtu.be/QH2-TGUlwu4)

Love it or hate it, we are gonna code it.

## [⏫ The Usual](#)

Create a script called `nyan` in the way that should be second
nature almost by now. Print your interpretation of “Nyan” but it
can be anything, within reason. Grab an 
[emoji](http://emoji.skilstak.io) for fun while you are at it
or import them, whichever you find easier.

```python
from emoji import cat
print(cat + " Nyan")
```

Add some color if you like.

> 💬 As a reminder make sure to stick with the names we say so
> that the links from your workbook will work.

## [⏫ True or False](#)

> Concepts: Booleans, Types, `True`, `False`

Before we continue let’s review what `True` and `False` actually
are. The big name for them is ***booleans***. A boolean is
something that is either `True` or `False`.

> 👓 The term Boolean comes from a English math guy name George
> Boole who was obsessed with logic and conditions.

How long is `True` `True`? How long is `False` `False`? Seems
silly to ask the question but that is exactly what we are
about to ask the computer in our script.

> 💬 The idea of true and false, on and off, 1 and 0 is found
> throughout computers and computer science because ultimately
> that is all a computer understands. Everything a computer
> does and knows can be reduced to a bunch of ons and offs.

## [⏫ Loop It](#)

> Concepts: `while`, Infinite Loops, End of the World

You may remember the `loop:` from CodeCombat. Well, that does not
exist in real Python. What you actually want is `while True:`
so let’s add that:

```python
while True:
    print(cat + " Nyan")

```
⛔ **DO NOT RUN YOUR PROGRAM YET!** First you have to learn to
stop it. Keep reading.

Here is that question, how long is `True` `True`? The answer
is forever, meaning this makes the computer print forever until
you kill it, the computer gets turned off, the power fails, or
the world we just so cordially greeted ends. Do not panic, there
are ways to stop your script besides ending the world, but we
need to go over some stuff first.

The `while` statement looks at the thing following it and will
continue to do whatever is in that *code block* as long as that
*condition* is true.

## [⏫ In Your Block](#)

> Concepts: Code Blocks, `:`

A ***code block*** is some amount of code that is grouped together.
The most common way to do this is with braces (`{}`) but Python
uses another way. **The colon character (`:`) when followed by a line
return and then finding the next line after it to be indented tells
Python to use all the lines that line up with that line as a code
block.** So in our script now we have only one line in our *code block*
that we could add to:

```python
while True:
    print("Nyan")
    print("Another Nyan")
```

You get the idea. These *code blocks* can be combined one within
another, which we will go over more later.

## [⏫ Indenting with `vim`](#)

> Concepts: `>>`, `<<`, `vim`

You probably just added spaces to the beginning of your `print()`
statement that you already had, which is fine. But there is another
way.

> 👓 To *indent* means to start a line of text further from the 
> edge, or margin, than the main part of text. By the way, to *indent*
> when starting a new line type the `TAB` key. In `vim` this makes
> it insert four spaces. There is no need to spam the space key (as
> some noobs do).

Since we have already typed out the print line you could just move it
over with `vim`’s `>>` shortcut. From command mode this inserts
enough spaces to ***indent*** properly. To move back the other
direction `vim` has the `<<` shortcut as well. Like all `vim` commands
these can be combined with numbers to operate on more than one line.
So `5>>` indents the five next lines from where you are in the file.

![](/assets/indenting.gif)

> 💬 Be careful if you are using an editor other than the one we
> have configured using [`home-config`][] because your `vim`
> might put an actual tab character in there, which no one does
> in the world of Python despite what anyone might tell you.
> This is particular true of the default Raspberry Pi NOOBS
> system that does not come with the latest `vim` by default.
> If you are using the Raspberry Pi, consider using one of
> our [SkilStak™ images][pi] to avoid this hassle of installing it.

[pi]: http://pi.skilstak.io
[`home-config`]: http://home-config.skilstak.io

## [⏫ Spaces and Tabs that Matter](#)

> Concepts: Significant White Space
 
Proper ***indentation*** is very important because Python uses
spacing as a part of the language, or, as they say, it is a
***significant whitespace*** language. Again, make sure your editor
is placing four spaces every time you tab.

> 💬 At one point the world fought bloody battles over whether white
> space should ever be a part of any language, turns out everyone
> settled down and more than a few still use the concept today

Why does whitespace matter? Because that is how Python identifies
a *code block*.

## [⏫ Make is STOP!](#)

> Concepts: Interrupts, `KeyboardInterrupt`, `ctrl-c`, Exceptions,
> `ctrl-z`, `ctrl-x`, Why NO `nano`

Time to run this, but when you do the first thing you will want to
know is how to make it stop. In fact, the main reason we are doing
this infinite loop is to learn how to stop something when it gets
out of control. The secret is `ctrl-c`, which sends an
`INTERRUPT` signal to the program stopping it.

> 👓 An *interrupt* is the same as in the non-programming world,
> something that stops something in the middle of what it is 
> doing. There are many ways a running program can be *interrupted*
> we just happen to be dealing with the `KeyboardInterrupt` at the
> moment.

![](/assets/keyboard-interrupt.gif)

Not very pretty, but it gets the job done. That ugly spew is called
an ***exception***. 

> 👓 An *exception* is an anomaly, abnormality; something unexpected
> that happens different from the normal flow. It might be an error,
> but maybe not, maybe it is just unexpected or is something you
> are not prepared to handle.

Usually you will program in ways to handle exiting your program
nicely, but not always. In fact, your users can do `ctrl-c` even
if you don’t expect it. This is why this is called an exception, 
but there is a way to make your program expect a `ctrl-c` and 
handle it better.

> 💬 This `ctrl-c` method will stop most anything that can be
> run from the
> command line. **Note this is NOT `ctrl-x`, which suspends the 
> process but keeps it running. Nor is it `ctrl-z`.** Students
> frequently confuse these and end up with problems—especially
> those unfortunate ones who have learned to use `nano`, which
> dubiously uses `ctrl-x` to close and save the file creating a
> horribly bad habit.

## [⏫ Catching and Trapping Exceptions](#)

> Concepts: Exceptions, `try:`, `except:`, Blue-Sky Scenario, `exit()`

The truth is there is a better way to stop your program than that
ugly exception. We *trap* it, or *handle* it, or *catch* it. These
are all terms for dealing with it. 

> 💬 I like *catch* the best because when you don’t the result looks
> like what you might expect when something falls without being caught.

![](/assets/catching-net.gif)

By adding the following `try` and `except` code we can tell Python
what to do with that annoying, ugly `KeyboardInterrupt`.

```python
try:
    while True:
        print("Nyan")
        print("Another Nyan")
except KeyboardInterrupt:
    print(c.clear + "Aw well")
    exit()
```

It almost looks like we put a net on its side around the code we
are running. By the way `exit()` just exits the program nicely.

![](/assets/trap-interrupt.gif)

Much less messy. 

> 💬 We cover exception handling much more as we go along
> but it is good to get a start understanding them now. **Exceptions
> are a common way most languages use to handle when things do not go
> as expected and give a way to program for those situations.** This
> also frees you to focus first on the “blue sky scenario” without
> being bogged down in all the possible ways your program could
> break.

## [⏫ Printing to Same Line](#)

> Concepts: `print()`, `end=" "`, `Line Buffering`, `flush=True`,
> `\n`, Line Returns 

You have probably noticed the `print()` function starts a new line
at the end of whatever you print out. Sometimes you want to not.
The parameter called `end` let’s you change that default from `\n`
to something else, say a space.

```python
        print("Nyan", end=" ")
        print("Another Nyan", end=" ")
```

Now the same looping, annoying word fills the whole screen.

![](/assets/print-end.gif)

### [⏫ Flushing](#)

There is one other detail about printing.

As silly as it sounds, flushing is the exact same thing you think
it is, just for the stuff to be printed out. To be more efficient
the computer stores up a full line of data before printing it out.
Depending on your system you can do a bunch of `print()`s like this
and not see the output at all for a while. To get around this you
can add another parameter `flush=True`.

```python
        print("Nyan", end=" ", flush=True)
```

Usually this is not a big deal but if it ever seems like something
is not printing as expected this is usually the problem.

## [⏫ Conclusion](#)

The infamous Nyan cat shows us about loops and what happens when
we cannot stop it. This comes up a lot when programming particularly
things that involve loops, which is pretty much every game ever
made.

## [⏫ Bonus Challenges](#)

💪 To flex those *string*, `print()`, and *join operator* skills
see if you can create an ascii art animation of your cat flying.
Make each frame a variable (constant) and print it after a `sleep()`
delay, then clear the screen and print the next frame and so on.
The secret will be having more than one `try/except` net.

💪💪 After you learn to define functions return and create a
`hmargin(colcount)` function to return the number of blank spaces
for the current terminal width to center the `colcount`. Hint, you
can call `tput cols` using the Python `subprocess` standard module.

💪💪 Create a `vmargin(linecount)` to return the number
of blank lines to vertically center a given number of text
lines (linecount). Hint, you can call `tput lines`
using the Python `subprocess` standard module.

💪💪 Use your new `hmargin` and `vmargin` functions to center
everything you are printing.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

