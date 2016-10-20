# [🍎 Welcome Teachers!](/README.md)

Whether you are a SkilStak™ senior student who has become a student
instructor, a teacher from a public or private school, a university
adjunct, or even from a corporate organization we welcome you and
hope you find this material useful. Like all courses and
learning modules at SkilStak™ each has a ***textbook*** and ***workbook***
GitHub repo. The *textbook* is for reference. The *workbook* is to be
used as a starter “assignment” repo for [GitHub Classroom][classroom].
You may wish to read more about using [*GitHub Classroom as Textbook
and Workbook*][text-work] to familiarize yourself with this approach.
We believe it is the future of all textbooks in education as the
OER movement continues and classrooms become more digital.

[classroom]: http://classroom.github.com
[text-work]: https://blog.skilstak.io/github-as-text-book-and-work-book-828ffada9542#.etr9ts7me

## Table of Contents

1. [**Prerequisites**](#user-content--prerequisites)
2. [**Age**](#user-content--age)
3. [**Time**](#user-content--time)
4. [**Rubrics**](#user-content--rubrics)
5. [**Resources**](#user-content--resources)
6. [**Encrypted Solutions**](#user-content--encrypted-solutions)
 1. [**Requesting Course Keys**](#user-content--requesting-course-keys)
 2. [**Alternatives**](#user-content--alternatives)
7. [**Other**](#user-content--other)
8. [**Next**](#user-content--next)
9. [**Contributing**](#user-content--contributing)
10. [**Copyright**](#user-content--copyright)

## [⏫ Prerequisites](#)

* Complete Prep

## [⏫ Age](#)

The content is designed with students ages 8 to 18 in mind but has
been completed by college age students and adults as well.

## [⏫ Time](#)

Students stay in this course until they are
[*certified*](http://certify.skilstak.io).  Our experience has shown
the average student can certify after about 100 total hours of time
invested in learning and practicing. The amount of time required
to certify will vary dramatically between individuals and has more
to do with the amount of practice students get outside of class
than aptitude or age.

There are only 16 weeks of 90-minute classes in a semester totaling
24 classroom hours 4 of which are *digital recess* time. It is
important to be realistic about how much mastery can be learned in
only 20 total hours of class time, yet this is still 20 times more
than most students get anywhere else.

Therefore, it should take students who do not do any work outside of
class five semesters (that’s two years if they attend all three
semesters). If a student spends 90 minutes at home working on stuff
outside of class that reduces the time in half, about one year. And if
the student spends three hours outside of class (and many spend *way*
more than that) it is realistic to see them certify in one semester.

We recommend focusing on incentives and motivation for students to work
on course projects or their own spin offs to maintain what they
learn through the week to get them as many hours as possible outside
of class.

## [⏫ Rubrics](#)

There are no rubrics other than instructor review of completed
course projects. All the solutions are available in the textbook
so [certification](http://certify.skilstak.io) is the main assessment
tool.

## [⏫ Resources](#)

Students need access to a **Bash command-line** on a computer that has
had **`python3`** installed. Usually this will be through an **`ssh`**
connection to a Linux account on a central school server but could
equally be done with [codeanywhere.com](http://codeanywhere.com),
individual Raspberry Pi computers, personal Linux laptops, virtual
machines, or a remote virtual host such as [Digital
Ocean](http://digitalocean.com).

The `lib/.lib` and `bin/.bin` directories contain libraries and
executables used by the lessons that the students need not understand
but can explore. Be sure to add these to the PATH as used by students.
The easiest way is to have them all using the same central, multiuser
Linux server with shell access and then add them to the system PATH.
The dotted, hidden directories are so that beginning students will not
see them with the `ls` or even the `ls -l` commands and be distracted.
Eventually, in more advanced classes the other version can be used.

## [⏫ Encrypted Solutions](#)

Fully coded solutions to each exercise have been included as [GnuPG][]
encrypted files. These solutions can–and should–be created by
following the steps of each lesson–even by potential teachers. This
encryption is mostly to keep extremely lazy students–and perhaps
even teachers who do not understand the material enough to teach
it–from simply copying and pasting code into their workbooks to
appear to have completed the assignment. Getting around the encryption
requires them to actually cheat if they want to get around actually
*doing* their work. Those that do will likely not pass certification.

[GnuPG]: https://www.gnupg.org/

### [⏫ Requesting Course Keys](#)

If you are an instructor or parent you can request the current
passphrase by emailing [learn@skilstak.com](mailto:learn@skilstak.com)
with “Request Course Key” in the subject line and a summary of who
you are and how you are using the material. Normally such things
would not be sent over email, but in this case we feel it is ok.
Your email will be added to a mailing list to which updated course
keys will be regularly sent.

```sh
gpg hello.gpg
```

After typing in the passphrase key when prompted this will produce
a `hello` file that can be `chmod +x`-ed, edited, and executed.

> ⛔ **For obvious reasons we ask that teachers not publicly distribute
> the unencrypted solutions. It is more of a practical matter than
> a legal one.**

### [⏫ Alternatives](#)

Of course as the instructor you can complete the assignments yourself
to produce your own solutions. This is actually optimal because it
ensures you understand the material and if you identify a problem can
help us improve it by opening an issue. However, we do understand not
all instructors and parents have this possibility and have therefore
made the encrypted solutions available.

## [⏫ Other](#)

Fundamentals is just that, fundamentals. Python comprehensions are
not a fundamental. Avoid the tendency to lose focus on the advanced
elements of Python at the expense of the fundamentals. There will
be plenty of time to explore the rest in
[Project](http://project.skilstak.io) after they certify.

## [⏫ Next](#)

After [certifying](http://certify.skilstak.io) students move to
[Project](http://project.skilstak.io) where they are prepared to
do learning modules from the [Engineering](http://eng.skilstak.io),
[Linux](http://linux.skilstak.io), [Data Science](http://data.skilstak.io),
and [Languages](http://lang.skilstak.io) focus categories.

## [⏫ Contributing](#)

We welcome any contributions or corrections to this material. If
you find a mistake or suggestion the easiest way is to submit an
issue on this textbook repo. However, if you would like to make a
more substantial addition consider forking this repo, making your
changes, and submitting a pull request to us. Any and all contributions
fall under the copyright license below ensuring all contributions
remain under the original copyright of this material such that they
can be enjoyed by all without fear or copyright violation.

## [⏫ Copyright](#)

![oer](/assets/oer.png)

This course is copyright [SkilStak, Inc.][skilstak] and released
under the Creative Commons Attribution-ShareAlike 4.0 International
License. You [should have received a copy of the license](LICENSE.md)
with this work. If not, see
[http://creativecommons.org/licenses/by-sa/4.0/][cc-by-sa].

We believe strongly in the *Open Educational Resources* (OER)
movement as promoted by [UNESCO](http://www.unesco.org), [OER
Commons](https://www.oercommons.org/), [MIT](http://ocw.mit.edu),
and others. Educators and course creators are encouraged to contribute
or modify this course under the terms of this license.

Students need not worry about copyright and licensing unless they
plan on publishing their own modifications or derived versions of
this course. Specifically they can use code created in their courses
in their own projects without fear of copyright infringement or
license violation. Student contributions to this or any other
SkilStak™ course are on behalf of SkilStak™ and become a part of
this copyright and license.
 ---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

