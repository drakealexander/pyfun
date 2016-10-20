# [⏪ Do You Like Waffles?](/README.md)


## Table of Contents

1. [**An Ancient Meme?**](#user-content--an-ancient-meme)
2. [**The Usual**](#user-content--the-usual)
3. [**Do you like waffles?**](#user-content--do-you-like-waffles)
4. [**Logic is a Little Tweeting Bird**](#user-content--logic-is-a-little-tweeting-bird)
5. [**The Difference Between Equality and Assignment**](#user-content--the-difference-between-equality-and-assignment)
6. [**A Big Nest**](#user-content--a-big-nest)
7. [**Trimming the Nest**](#user-content--trimming-the-nest)
 1. [**Why not just use `if answer == "no"`?**](#user-content--why-not-just-use-if-answer--no)
8. [**Notice Any Patterns?**](#user-content--notice-any-patterns)
9. [**Defining Our First ~~Procedure~~ Function**](#user-content--defining-our-first-procedure-function)
 1. [**Assertions**](#user-content--assertions)
10. [**Handling the Other Exceptions**](#user-content--handling-the-other-exceptions)
 1. [**Blue Sky Path and Exceptional Path**](#user-content--blue-sky-path-and-exceptional-path)
11. [**Speaking of Lists (and Tuples)**](#user-content--speaking-of-lists-and-tuples)
12. [**Exception: User Enters Variation of `yes`**](#user-content--exception-user-enters-variation-of-yes)
 1. [**Beware of Thinking Like a Human**](#user-content--beware-of-thinking-like-a-human)
 2. [**The `.lower()` String Method**](#user-content--the-lower-string-method)
 3. [**Looking in Tuple Instead of Compound Condition**](#user-content--looking-in-tuple-instead-of-compound-condition)
 4. [**Checking the Beginning with `.startswith()`**](#user-content--checking-the-beginning-with-startswith)
 5. [**Other String Methods**](#user-content--other-string-methods)
13. [**Exception: User Includes Spaces**](#user-content--exception-user-includes-spaces)
14. [**Exception: User Interrupts with `ctrl-c`**](#user-content--exception-user-interrupts-with-ctrl-c)
15. [**Conclusion**](#user-content--conclusion)
16. [**Bonus Challenges**](#user-content--bonus-challenges)

## [⏫ An Ancient Meme?](#)

Ok, so maybe not a meme, but definitely a phenomenon now with over 24
million views on, what one commenter calls it “good ’ol 2008 YouTube”
(as if that were a long time ago).

[![](/assets/waffles-youtube.gif)](https://youtu.be/eDU0CTDMk2g)

Well we are happy to keep the ad revenue pouring in to Nathan and
Parry as best we can by coding their video.

## [⏫ The Usual](#)

> Concepts: Boilerplate, `bin`

Yeah, yeah, you know what to do. The name should be `waffles` this
time, of course. In fact, you can literally just copy the `hi` script
to `waffles` to save time.

```sh
cp hi waffles
```

> 💬 By now you should be getting blazing fast at getting a script
> setup for the rest of the coding.

> 💪 Create a `bin` directory and create a Python script that
> prints out the ***boilerplate*** for a basic script (ex: shebang
> line, initial comment, `print()`). You can later put this in your
> home directory `bin` so you can use it anytime to create a new
> Python script. This technique is common in the industry and saves
> a lot of time overall. So long as it does not include specific code
> for a given assignment you can even use this to reduce your times
> and prepare for the [certification
> exam](http://certify.skilstak.io).

> 👓 Boilerplate is a term that came from the newspaper industry back
> when they literally boiled lead creating a part of the paper that
> could not be altered. Lawyers picked up on the term and used it
> for parts of a contract that could be included verbatim every time.
> Somehow eventually coders adopted the term for segments of code that
> don’t change or that once can start out with and modify while
> keeping the form.

## [⏫ Do you like waffles?](#)

> Concepts: `input()`

You already know how to ask a question. Something like this, right?

```python
#!/usr/bin/env python3

print("Do you like waffles?")
answer = input("> ")
print(answer)
```

![](/assets/waffles-input.gif)

> 💬 Remember you can always make it more aesthetically pleasing with
> color and emojis we just show the minimum. Usually it is a good
> idea to get stuff working before making it pretty—in anything.

## [⏫ Logic is a Little Tweeting Bird](#)

> Concepts: Logic, `if`, `else`, Conditions

We humans have it pretty good. Our heads don’t explode when we have to
deal with something like the *Liar’s Paradox*.

[![](/assets/illogical.gif)](https://youtu.be/wlMegqgGORY)

So what *is* logic, other than a “little tweeting bird” that is?

> 👓 Logic has many meanings but in computer science it refers to the
> decisions a script has the computer make in order to fulfill
> a set of instructions. Another important word ***algorithem*** is
> this collection of instructions.

> 💬 Logic is the main thing that distinguishes a *programming*
> language from a *markup* or other coding language. If the language
> has an `if` in it then it is usually *programming*. We went over
> this distinction back in [Prep](http://prep.skilstak.io) but good
> to review.

Let’s add an `if` statement. This is the main point of this lesson.

> 💬 A ***statement*** is any keyword from the language. 

```python
print("Do you like waffles?")
answer = input("> ")
if answer == "yes":
    print("Awesome!")
else:
    print("Fine.")
```

> 💬 You should remember this from CodeCombat during
> [*Prep*](http://prep.skilstak.io).

The `answer == "yes"` part is a *condition*. If the condition is
`True` then `Awesome!` is printed, otherwise (`else`) `Fine.` is
printed.

> 👓 A ***condition*** is the state that something is in. Thankfully in
> computer science there are only two possible states, `True` and
> `False`, which you will remember from the [Nyan](/nyan/README.md)
> lesson.

## [⏫ The Difference Between Equality and Assignment](#)

> Concepts: `=`, `==`, Is Equal To, Assign 

We covered [assignment in *Hi
There*](/hi/README.md#user-content--where-is-your-assignment) but now
we have two equals signs. These `==` mean “is equal to” and are pretty
universal in all programming languages. (JavaScript even has another
with three `===`.)

> 💬 This difference confuses everyone when they first see it without
> having this explanation. Consider yourself enlightened.

## [⏫ A Big Nest](#)

> Concepts: Nested Code Blocks, Shallow Nesting by Design

Adding the other possible breakfast foods will get interesting. You
do not have to code this, just make sure you understand what it is
doing.

```python
print("Do you like waffles?")
answer = input("> ")
if answer == "yes":
    print("Do you like pancakes?")
    answer = input("> ")
    if answer == "yes":
        print("Do you like French toast?")
        answer = input("> ")
        if answer == "yes":
            print("Do, do, da, doop, can’t wait to get a mouthful.")
        else:
            print("Well I like French toast.")
    else:
        print("Well I like pancakes.")
else:
    print("Well I like waffles.")
```

So, um, do you see the resemblance? 

![](/assets/nested-python.gif)

Yeah, that’s where it comes from. At least maybe you will remember
the term *nesting* better now. Here is what it does, which is what
you would expect.

![](/assets/waffles-nested.gif)

I bet you can already see that we repeat ourselves waaaay too much.
Time for some trimming.

## [⏫ Trimming the Nest](#)

> Concepts: Refactoring, Code Maintenance, Code Organization,
> Program Design, Spaghetti Code, Conditional Modifiers, `not`, 
> Checking for Good not Bad

Big nests might be be good in the wild, but not when programming.
They get really hard to follow and maintain. Perhaps the worst is
when there are `else` clauses involved because they might not be
anywhere near the if statement any longer and completely off the
screen.  When and if you ever see this kind of spaghetti you will
really know it.

> 👓 The term ***spaghetti*** here is anything but delicious. Its
> a pejorative term for code that is an ugly mess that brings those
> who have to maintain it to wish very bad things on the coder who
> left them with the *spaghetti* to maintain or clean up. Start now to
> write clean code, or at least to clean it up after you get your idea
> off the ground. (Premature optimization is also bad since it will
> slow your development.)

> 💬 All the work we do to make our big nested version better is called
> ***refactoring***, which is a fancy way of saying to simplify,
> clarify, and generally better organize our code. This is what you
> spend most of your time doing as a coder, by the way. Code is
> maintained and changed much more than it is originally written.

When you want to move code you cannot just cut and paste it. You
have to change all the indenting, which can be a real pain depending
on what editor you are using.

> 💬 You will remember we covered [indenting with `vim` in
> `nyan`](/nyan/README.md#user-content-indenting-with-vim)

So let’s trim this down, but how. First let’s put all the `if/else`
blocks as far to the left as we can get them and change our
*condition* to check for the opposite of `yes` or `not answer ==
"yes"`. That’s right, `not` is a ***conditional modifier*** and
switches whatever the *Boolean* was to its opposite, so `False` to
`True` and `True` to `False`.

> 💬 In other programming languages the `not` *conditional modifier* is
> usually a single exclamation point `!`. Python prides itself on
> readability and we are very thankful for it.

```python
print("Do you like waffles?")
answer = input("> ")
if not answer == "yes":
    print("Well I like waffles.")
    exit()

print("Do you like pancakes?")
answer = input("> ")
if not answer == "yes":
    print("Well I like pancakes.")
    exit()

print("Do you like French toast?")
answer = input("> ")
if not answer == "yes":
    print("Well I like French toast.")
    exit()

print("Do, do, da, doop, can’t wait to get a mouthful.")
```

### [⏫ Why not just use `if answer == "no"`?](#)

The simplest way to understand why is to think of a password or key
in the physical world. There are only a few that will work and an
infinite number of others that won’t. So the simpler—and more
secure—question to ask is, **“Which is *not* allowed, not ‘good’?”**

> 💬 This concept might seem incredibly obvious but you would be
> shocked to see all the code out there that does exactly the wrong
> thing by trying to catch all the “bad” characters or code rather
> than checking for only “good” ones. If you have ever heard of SQL
> injection attacks on web sites, well, that is one area where this
> has happened a lot. Moral of the story: check for good, (or not
> good), not bad (or not bad).

## [⏫ Notice Any Patterns?](#)

> Concepts: Redundancy, Variables, Assertions, The Dude

I think this super-coder notices some lack of laziness that he cannot
“abide.” (The computer science Ph.Ds call this *redundancy*.)

![](/assets/dude.png)

For the sake of demonstration (don’t do this) I will replace all the
parts of this code that are different with a *variable*. Here is where
the term *variable* really shines because all the stuff I am replacing
*varies* in each section.

```python
food = "waffles"
print("Do you like " + food + "?")
answer = input("> ")
if not answer == "yes":
    print("Well I like " + food + ".")
    exit()

food = "pancakes"
print("Do you like " + food + "?")
answer = input("> ")
if not answer == "yes":
    print("Well I like " + food + ".")
    exit()

food = "French toast"
print("Do you like " + food + "?")
answer = input("> ")
if not answer == "yes":
    print("Well I like " + food + ".")
    exit()

print("Do, do, da, doop, can’t wait to get a mouthful.")
```

Wait, do you see what I see? Every single section is identical
except for the *variable*. I love that word, *variable*, *variable*,
*variable*.

If only there were a way to only write that code once and change the
variable every time we want to run it, hummm.

## [⏫ Defining Our First ~~Procedure~~ Function](#)

> Concepts: Defining Functions, Python Style Guidelines, PEP-008

Turns out there is a way, define a ***function*** containing the code
in its *block*. Then you can call it three times for each food.

```python
def check_if_likes(food):
  print("Do you like " + food + "?")
  answer = input("> ")
  if not answer == "yes":
      print("Well I like " + food + ".")
      exit()

check_if_likes("waffles")
check_if_likes("pancakes")
check_if_likes("French toast")
print("Do, do, da, doop, can’t wait to get a mouthful.")
```

> 💬 Remember when we went over
> [Actions in our first *Hello World!*
> program](/hello/README.md#user-content--action)?
> You might remember the technical difference between
> a function and a procedure, which no one really distinguishes
> anymore but we can for grins.

### Keeping Python Stylish

When you hear the word *style* you probably think of clothes more than
you would code and programming but, believe me, there is plenty of
room for style in your code. 

The single most important thing to remember when dealing with style
is **do not vary the style from the code that is already there**.
This will get you shot in some programming circles. I am just looking
out for you.

If there is a second law it is *thou shalt use the style guide for the
given language* if there is one. Thankfully there is a very clearly
defined Python standards organization and a very clear standard about
style. It contains everything from how many spaces to use, to how to
name your functions, variables, and classes. The bottom line, **use
it!** You will have a very difficult time justifying your choice not
to follow the standard. Most of the time your code contributions will
quietly be ignored and you will be marginalized silently by those who
see you have no desire or understanding of the standard. Do not let
that be you. Those impressions are very hard to undo.

> 💬 It is still virtually unbearable to see mixed case variable and
> function names used in CodeCombat.com and several popular O’Reilly
> technical books when the [standard very clearly states using
> underscores is preferred][naming].

[naming]: https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions

Take a moment eventually and read all of the [Python PEP-0008][pep]
conventions so you start out right.

[pep]: https://www.python.org/dev/peps/pep-0008

### [⏫ Assertions](#)

***Assertions*** are functions or statements that check a condition
and if `False` blow up the program by throwing an exception or just
existing. You can create assertion functions that just return values,
but what we have now with our `check_if_likes()` is a classic
*assertion*. It is really a matter of style what you name this
function. You can keep the name you have, or consider something like
the following:

```python
def assert_likes(food):
  ...

assert_likes("waffles")
assert_likes("pancakes")
assert_likes("French toast")
print("Do, do, da, doop, can’t wait to get a mouthful.")
```
> 💬 The main reason for doing this is that when an experienced programmer
> sees the word `assert` in something they expect stuff to blow up if
> the assertion fails. `check_if` is not really clear about what it does
> if the check is `False`.

Assertions are big part of writing test code, so much so, in fact,
that Python has included the `assert` *statement* as a part of the
language. We can use this to come up with an entirely different form
of our program. It is mostly a matter or preference, either is correct
and both are good design.

> 💬You already know how to catch an exception from
> [Nyan](/nyan/README.md#user-content--catching-and-trapping-exceptions).

```python
try: 
    assert input("Do you like waffles? ") == "yes"
    assert input("Do you like pancakes? ") == "yes"
    assert input("Do you like French toast? ") == "yes"
except AssertionError:
    print("Well I do.")

print("Do, do, da, doop, can’t wait to get a mouthful.")
```

> 💬 This gives us the bare-bones functionality required, but will not
> easily support the other things we still want to do, color
> and emojis and screen positioning.

## [⏫ Handling the Other Exceptions](#)

> Concepts: Blue Sky Path, Blue Sky Scenario

What if someone says no? What if they say something other than "yes"
that means yes? What if they *interrupt* the program with a
`ctrl-c`? 

![](/assets/waffles-no.gif)

### [⏫ Blue Sky Path and Exceptional Path](#)

In software architecture (yes it is the same as when people build
buildings, just with software) there is a term called ***blue sky***
combined with ***scenario***, ***story***, or ***path***. This
refers to the best case, or sometimes even the base case, the main
expectation of the code if everything goes well, if no one does
anything unexpected, if the user can be trusted. 

> 💬 We have already gone over [exceptions in
> Nyan](/nyan#user-content--make-is-stop).

Good coders always code the *blue sky* first and then begin layering
on all the ***exceptional paths***, those things that can go wrong or
might not be expected, but can happen.

> 💬 Getting bogged down in *exceptional path* programming too early
> in the software design and development phases can seriously slow
> you down and often unnecessarily. Say you code all the exceptional
> cases for a given part of your program, then you realize you did not
> even need it later in your *blue sky*. You wasted all that time.
> Like a good artist, rough your programming creation in with sketches
> and broad strokes knowing that the rest of the detail will come in
> later. In case you haven’t noticed yet, that is why all this course
> code does not have the coloring and emojis in the code even
> though they are in the final output.

## [⏫ Speaking of Lists (and Tuples)](#)

> Concept: Lists, Tuples, `[]`, `()`, Immutable

Ok, so we were not actually speaking about lists yet, but we sure
are going to be. So might as well go over them now.

A ***list*** is exactly what it sounds like, a bunch of things one
after the other separated by commas. Square brackets show where the
list begins and ends. You can combine different types of things in
the list, numbers, strings, booleans, even other lists and function
references.

```python
def sent():
    print("I was sent")

mylist = ["some", 1, True, "was", [sent, 4, 'u']]
```

> 💬 Lists are universal to programming and are often called
> ***arrays*** in other languages (gotta love Python).

> 💬 Normally a lot of textbooks would cover ***list comprehensions***
> somewhere around here but we will hold off until you have more
> practice. They are basically in-line `for` loops, which we go over
> later in [Badgers](/badgers/README.md).

A ***tuple***, [pronounced TYOU-pul](https://youtu.be/CwhBc39OyWA), is
a list that cannot be changed. Here’s a word you probably haven’t
heard, ***immutable***. It means can’t be mutated, or changed.
Everything else about them is the same as lists.

```python
def sent():
    print("I was sent")

mylist = ("some", 1, True, "was", (sent, 4, 'u'))
```

> 💬 Sometimes when using a function you will get an error saying it
> does not allow a list and requires a *tuple*. All you have to do is
> change the brackets `[]` to parentheses `()`.

## [⏫ Exception: User Enters Variation of `yes`](#)

> Concepts:  Compound Conditions, `or`, `and`, Logic Errors,
> `.startswith()`, `.lower()`, `in`, Methods v.s. Functions,
> String Methods, Order of Operations, `()`, Regular Expressions

So there is definitely more than one way to say 'yes' beginning with
'Yes', 'YES', and the rest. We could do something like this:

```python
if not (answer == 'yes' or answer == 'Yes' or answer == 'YES'):
    ...
```

We have to add the parentheses around all the `answer == ` conditions
so that `not` will check them all and then reverse it. In math the use
of parentheses in this way is called ***order of operations***. By
placing them we tell Python what to do first. In this case, first
check all the conditions, then reverse the result with `not`.

### [⏫ Beware of Thinking Like a Human](#)

You will notice the `or` connecting the *conditions* creating
a ***compound condition***. 

> ⛔ Note `answer ==` is repeated in each *condition*. There is a real
> temptation to attempt `answer == 'yes' or 'Yes' or 'YES'` but this
> is incorrect. Python needs each condition spelled out. This is
> particularly dangerous because the **incorrect version will not
> produce an exception**, it is technically correct, but logically flawed.
> This is because `'Yes'` *is* a condition that becomes `True`, but it
> is *always* `True`. 

![](/assets/yes-no-true.gif)

### [⏫ The `.lower()` String Method](#)

Before resorting to a *list* or *tuple* we can cover all three of the
conditions above with one change.

```python
if not answer.lower() == 'yes':
    ...
```

The `.lower()` is a ***string method***. A ***method*** is essentially
a *function* that is tied to thing by the dot `.`. That thing is the
first argument to the function. In a very literal way,
`answer.lower()` is the same as `lower(answer)`, if it existed.

> 💬 We will see later why chaining methods is easier to read and
> understand than the alternative (i.e. `answer.lower().strip()` v.s.
> `strip(lower(answer))`)

> 💬 Congratulations you have written your first ***object oriented***
> code. The term *method* is from that paradigm of programming. If you
> have not yet heard of OO no problem, if you have, just know that is
> what all this *method* stuff is about. The *string* `answer` is the
> object. 

### [⏫ Looking in Tuple Instead of Compound Condition](#)

We still have a problem though. What if someone enters 'yep' or 'of
course'? The `answer.lower()` does not cover that. Thankfully there is
the ***`in` operator***. 

```python
if not answer.lower() in ('yes', 'yep', 'of course'):
    ...
```

Go ahead and try to change your code to use `in` with a tuple of
different possible `yes` variations.

> 💬 Always use a *tuple* whenever you can because they are far more
> efficient. Python deals with them very differently internally
> for than it does a list, which can change at any point during the
> run of the script.

If you have a lot of them you can put all the 'yes' versions into
another variable, we will call it `yes`.

```python
yes = ('yes', 'yep', 'of course', 'positively', 'affirmative', 'ok')
if not answer.lower() in yes:
    ...
```

We can do another cosmetic change to make it read a little easier.
This reverses the result of the *condition* `in yes`.

```python
if answer.lower() not in yes:
```

### [⏫ Checking the Beginning with `.startswith()`](#)

Smart users might type 'yeppers' or 'yes, of course', or 'ok I guess'.
We can out smart them with the `.startswith()` method, which does
exactly what it appears to, takes one argument, a *tuple*.

```python
if not answer.lower().startswith(yes):
    ...
```

Now we are really getting somewhere.

### [⏫ Other String Methods](#)

Before we leave the topic of *strings* as *objects* and their
*methods* it is worth noting there are literally dozens of
different ***string methods*** for dealing with all sorts of
possibilities from the most simple to the most complex.

> 💬 Google 'python string methods' to learn more. (You need to become
> very proficient searching things like this to succeed as a coder.)

> 💪💪💪💪 The most complex string matching and manipulation is done with
> its own sub-language of sorts called ***regular expressions***.
> Regexs are in *every* language these days and were perhaps most
> popularized in Perl, which remains the gold standard for regexs.
> Even Python used the Perl style of them. Learning them will be
> phenomenally valuable to you but will likely permanently separate
> you from all your programming peers. Be careful if you decide to
> learn them because of this. Python has so many string methods that
> using regular expressions is usually overkill, but when you need
> some 20th level string magic, they are available if you choose to
> learn them. If you wind up doing most of your code manipulating and
> interpreting text than it is a really good idea to master them.

## [⏫ Exception: User Includes Spaces](#)

> Concepts: Trimming Whitespace, `.trim()`, `.ltrim()`, `.rtrim()`

What if the user purposefully or accidentally types in some spaces or
tabs before or after their answer before entering it?

![](/assets/waffles-no-trim.gif)

Yep, so we catch 'yeppers' but can still be broken with a simple
space. Hummm. Sounds like we need the `.trim()` *string method*.

```python
if not answer.trim().lower().startswith(yes):
    ...
```

The `.trim()` method removes any whitespace characters, like spaces
and tabs, from *both sides* of the string. The `.ltrim()` and
`.rtrim()` do just one side as you would expect.

> 💬 Would you believe it is as simple as that? Python is pretty amazing.
> Try that in C, lol, reminds us why ***higher level languages***
> like Python are needed. They are closer to the way we humans speak
> and understand the world.

## [⏫ Exception: User Interrupts with `ctrl-c`](#)

> Concepts: Catching Multiple Exceptions, `except`, `KeyboardError`

Finally, the bomb, catching the ugly `KeyboardInterrup` but you
[already know how to do
that](/nyan#user-content--make-is-stop). How do you combine catching
the `AssertionError` with another? Let’s go back to our earlier
version that uses the `assert` keyboard to demonstrate how. We could
add it simply to the same one.

```python
except AssertionError, KeyboardError:
    ...
```

Or we could make a line just for the `KeyboardError`:

```python
except AssertionError:
    ...
except KeyboardError:
    print("Well, fine.")
    exit()
```

That is right. You can have blocks for each individual exception that
might possibly be thrown (also known as **raised**).

## [⏫ Conclusion](#)

As usual we have taken a fun, relatively plain program and used it
to cover some major programming skills and concepts. At this point you
should understand enough to make some rather interesting programs of
your own.

> 🍎 It is usually at this point that students want to jump off into
> their own text adventure or combat game script. Nothing wrong with
> that as long as they realize there are still more concepts to come,
> and just such an adventure is one of our final projects later.

## [⏫ Bonus Challenges](#)

All of these bonus challenges are not core to the requirements of the
program. Like good worker/programmer types working for potential
bosses we never add all this flare until after the core requirements
are met. Now we can have fun with all the flashy stuff.

> ⛔ **Never sacrifice stability for flash.** If you cannot add the
> cool stuff and adequately *regression test* it to prove you have not
> broken something in the process then do not add it, ever. (Now if
> someone could invent a Smart Phone that can actually make stable,
> clear calls like some can remember land lines did.)

💪 See if you can ask about several other foods and make a pause
between all the do, do, da, dos at the end that matches the timing
of the song using multiple `print()` functions with `end=" "` and
a `time.sleep()` for each.  You can even make a `paused_print(thing,pause)`
function that takes two arguments, the thing to print and the delay
to pause after each.

💪 Do both verses. Print something special after last verse.

💪 Add a `KeyboardInterrupt` trap to exit nicely if the user tries
to bail out.

💪 Add a music emoji of some kind to imply music. Hint, you will
have to change certain items in the list every time by indexing
them.

💪💪 Add screen centering like you may have done in [Nyan](/nyan/README.md).

💪💪 Create a list (or tuple) of tuples with the first item being the
word and the second item being the pause and limit yourself to a
single `paused_print()`s call in a for loop.

💪💪 Using the math operator create a `tempo` variable and `w`, `wq`,
`q` note variables that are fractions of the tempo and use those
for the pauses.

💪💪💪 Download your script to a local Mac with `say` enabled and see
if you can get the computer to say what it is asking and printing.
You will have to research how to call a command line program from
within your Python. (Google is not cheating.)

💪💪💪💪 Convert the questions to ***lists*** (not tuples) in a global
list of words and print out the words of the questions in the song
to the beat that they are asked. Change the `assert_likes()` function
to accept a list of two syllable foods. Replace the last two items
in the `verse` list with the syllables of the food passed as a list
argument to `assert_likes()`.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

