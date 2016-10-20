# [⏪ Badgers, Badgers, Badgers](/README.md)

In this lesson you learn how to teach your program to count and 
repeat stuff for a specific number of times.

## Table of Contents

1. [**The Usual**](#user-content--the-usual)
2. [**How many badgers is that again?**](#user-content--how-many-badgers-is-that-again)
 1. [**How Long is True, True?**](#user-content--how-long-is-true-true)
 2. [**Everything Must Come to an End**](#user-content--everything-must-come-to-an-end)
3. [**Teaching Our Program to Count**](#user-content--teaching-our-program-to-count)
 1. [**Creating a `count` Variable for Remembering**](#user-content--creating-a-count-variable-for-remembering)
 2. [**Adding One to the Count**](#user-content--adding-one-to-the-count)
4. [**But Mom, the Program Says Raise My Allowance**](#user-content--but-mom-the-program-says-raise-my-allowance)
5. [**Conclusion**](#user-content--conclusion)
6. [**Bonus Challenges**](#user-content--bonus-challenges)

## [⏫ The Usual](#)

You [know what to do](/hello/README.md). Create a script and have
it print something just to make sure everything is setup correctly
before we continue.

## [⏫ How many badgers is that again?](#)

> Concepts: Counting, Infinite, Finite, Boolean, `while`,
> Algorithms

Let’s take a look. Can you count them?

[![](/assets/badgers.gif)](https://youtu.be/EIyixC9NsLI)

Ok, so there are 12 of them, 2 mushrooms, and a snake:

* repeat 3 times:
  * 12 badgers
  * 2 mushrooms
* 12 badgers
* 1 snake
* repeat 4 times:
  * 12 badgers
  * 2 mushrooms
* 12 badgers
* 1 snake
* 12 badgers
* 2 mushrooms

These verses of the “song” will be our simple algorithm. Let’s code it
and learn about ***finite loops*** in the process. These loops only
repeat for a certain number of times.

> 💬 You will remember we already learned about the
> infinite version of the `while` loop (`while True`) in
> [Nyan](/nyan/README.md). That is where we learned the term
> [Boolean](/nyan/README.md#user-content--true-or-false)
> as well.

### [⏫ How Long is True, True?](#)

Duh, forever right. Yeah that is a long time. That is ***infinite***.
It never ends. There are other things that are infinite as well, like
`1 == 1`, `2 + 2 == 4`

> 💬 Don’t ever let anyone tell you there are not absolute truths in
> the universe. There are.

### [⏫ Everything Must Come to an End](#)

Stuff that has an ending is ***finite***, like our lives, our program,
and each verse of the song. Things that are ***finite*** can be
measured and counted. This is what we will do in this program.

## [⏫ Teaching Our Program to Count](#)

> Concepts: Addition Operator, `+`, Augmented Assignment, `+=`

Computers are, as Lord Gabe Newel (of Valve) says,
“possibly the stupidest thing in the entire universe.”

[![](/assets/gabe-stupidest.png)](https://youtu.be/dU1xS07N-FA?t=9m30s)

*(Thanks again to Code.org for the video.)*

It is not rude or incorrect to say that a computer knows *nothing*
unless we teach it. In order to have our program stop after a certain
number of repeated verses we first have to teach it to count.

### [⏫ Creating a `count` Variable for Remembering](#)

> 💬 We already learned how to make our program remember stuff with
> *variables* in [*Hi
> There!*](/hi/README.md#user-content--teaching-a-computer-to-remember).

Let’s start by making our program remember a single number we will
call `count`. We will put the number 0 in it.

```python
count = 0
print(count)
```

So far we are not doing anything with `count`, just making sure it
is getting *assigned* correctly.

### [⏫ Adding One to the Count](#)

To tell our program to add one to `count` we use the ***additional
operator***, the fancy name for plus `+`.

```python
```

> 💬 This is the first time we have done actual math in our program but
> we have seen the plus sign `+` before as the [join
> operator](/hello/README.md#user-content--beads-on-a-necklace)

## [⏫ But Mom, the Program Says Raise My Allowance](#)

> Concepts: Difference Between Join and Addition Operators, Chores,
> Allowance

Even though we have not yet learned all the other math operators the
fact that they can be used on *numbers or strings* produces some fun
results.

![](/assets/allowance.gif)

There is a fun prank we like to imagine to show the difference between
the two versions of the plus sign `+`. It goes like this. Pretend you
are negotiating a raise in your allowance with your Mom or Dad. You
get a dollar now and figure you could write a program to impress them
with that suggests how much your chores are worth. They agree because
it is so awesome that you are coding at such a young age. You tell
them you only want one dollar a week and for some reason they let
you write a program to calculate your allowance for a 4-week month,
(shhhh, I know there is an easier way). The multiplication operator is
an asterisk So you quickly write a
program like the following:

```python
print("Enter the amount per week.")
weekly = input("> ")
print(weekly * 4)
```

![](/assets/allowance-prank.gif)

Woot! 

## [⏫ Conclusion](#)

Could the Badgers have taught us a lot about the nature of the
Universe? Perhaps, but mostly they taught us how to teach our programs
to count and do things after counting to certain numbers.

> 🍎 Do not confuse finite counting loops with list iteration, which we
> cover later.

## [⏫ Bonus Challenges](#)

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

