
# Script for the BSD Video

**Author:** cw

---

## Elliptic Curves

### Te will explain BSD

1. **st + te** centred on background
2. **st:** I have heard about the Riemann hypothesis (bubbles with `$\zeta(s)$`).
   You are a number theorist. Are you working on this?
3. **te:** Not directly. My research concerns another important conjecture,
   also worth a million dollars (bubble `$\zeta(s)$` is kicked out for an elliptic curve).
4. **st:** What is it?
5. **te:** The Birch and Swinnerton-Dyer conjecture. (**Title** The Birch and Swinnerton-Dyer conjecture)
6. **st:** Can you explain?
7. **te:** Sure. (Bubble increases, characters stay in the bubble until the whole screen is in the bubble. Characters also move to the lower-left corner.)

---

### Define elliptic curves
(**Title** Elliptic curves)

1. **te:** It deals with equations like `$y^2 = x^3 - 4x + 1$`, called elliptic curves (centred).
2. **st:** What do they look like?
3. **te:** Here. (Equation moves up left, curve appears.)
4. **st:** What are other examples?
5. **te:** We need `$y^2 = x^3 +$` some integer times `$x$` plus another integer.` (Equation and picture show other curves with coefficients framed.)
6. **te:** Some are formed of two pieces some only are only one piece (Goes through a family of curves whose discriminant switches sign.)
7. **st:** They are all symmetric? (Back to `$E$`, symmetry shows)
8. **te:** Yes, as `$y$` only appears as an even power (`$(-y)^2 = y^2 = \dots$`).

---

## Rational Points on Projective Curve

### Rational points
(**Title** Rational points)

1. **st:** What do you study about them?
2. **te:** I count solutions to the equation with both `$x$` and `$y$` rational (`$x,y \in \mathbb{Q}$` appears).
3. **st:** Hmm (thinks), like when `$x=0$` then `$y=1$`. Or `$y=-1$`. (Highlight these points)
4. **te:** Yep. I chose an example with a lot of solutions. (Points are highlighted successively, including one really complicated example.)
5. **te:** Some lie outside the screen (?). Some other elliptic curves have very few rational points.
6. **st:** Looks hard to find them.

---

### Projective curve
(**Title** ?)

1. **te:** We can write `$x = X/Z$` and `$y = Y/Z$` with integers where `$Z$` is the least positive common denominator. (The equation transforms to substitute, move power.)
3. **te:** Multiply by `$Z^3$`. (Get to the projective equation `$Y^2Z = X^3 - 4XZ^2 + Z^3$`.)
4. **st:** I know this is a projective curve.
5. **te:** Indeed. We can now study integer solutions `$X, Y, Z$` to this equation instead.
6. **te:** But if we do, do we get extra solutions — like when `$Z$` is negative?
   We need to identify solutions when they are scalar multiples of each other (`$(X,Y,Z) = (-X,-Y,-Z) = (2X,2Y,2Z)$` since `$x = X/Z = -X / -Z = 2X / 2Z$`).
7. **te:** And we have accidentally added a new point — the one with `$Z=0, X=0, Y=1$`.
8. **te:** To visualize it as a point infinitely far away, we should have a look at the horizon. (Turn to 3D scene where the usual plane flips down.)
9. **st:** Wow. (surprise) (2D flat characters stay in plane / What if they are 3D?)
10. **te:** No worries. Now we see the unique point at infinity and — look — the horizon is a tangent to our curve. (Point to `$O$`)
11. (Undo the flip back to 2D.)

---

## Count Points

### Counting rational points
(**Title** Counting rational points)

1. **te:** The conjecture is about counting rational solutions.
2. **st:** There are only finitely many? (surprised)
3. **te:** No! (reassuring) Well, for some curves like `$y^2 = x^3 - 4x - 2$` there are only four points. (Plot the curve a point out the 4 points.)
4. **te:** But for our example `$E$` there are infinitely many solutions.
5. **te:** We count them by the size of the integers involved.
6. **te:** For instance, there are 15 solutions with `|X|, |Y|, |Z| < 10` (list them) and 27 smaller than 100 (list those).
7. **te:** We call `$N(T)$` the number of points with integer coordinates below $T$   (Definition of `$\mathcal{N}(T)$` appears .)
7. **st:** I see, these are the first solutions we would find if we search for them with a computer.
8. **te:** Yep. Searching in a box I'd call it.

---

### Counting modulo
(**Title** Counting points modulo)

1. **te:** This counting will be compared to counting modulo.
2. **te:** We look for integers such that both sides have the same remainder when dividing by — say — 10. (Affine points coordinates appear)
3. **st:** You solve `$y^2 = x^3 - 4x + 1$` modulo 10.
4. **te:** Ehmm, yes, but also the points at infinity as there might be more than one. (Projective equation modulo 10.)
5. **te:** There are 27 solutions modulo 10, of which 11 are at infinity. (The additional projective points appear.)
6. **te:** Again, we identify solutions `$(X,Y,Z)$` that were scaled by 3, 7, or 9 — the invertible elements in `$\mathbb{Z}/10\mathbb{Z}$`.
7. **te:** We define `$M(U)$` as the number of solutions modulo an integer `$U$`. (Definition of `$\mathcal{M}(U)$` appears)
8. **te:** As `$U$` increases, the number of solutions modulo `$U$` grows. (Bar chart of values of `$\mathcal{M}(U)$`)

---

## Conjecture

### State conjecture
(**Title** The conjecture)

1. **te:** Recall `$\mathcal{N}$` and `$\mathcal{M}$`. (Their defintions appear on the right half).
2. **te:** Pick `$T$` large and set `$U$` to be `$T$` factorial. (Shows up and $U$ transforms to `$T!$)
3. **st:** If `$T$` is biiig, `$T!$` is huuuuge.
4. **te:** Put `$\mathcal{N}(T)$` on top of a fraction, and square it. (Copy over to fraction and add suare)
5. **te:** We compare to `$\mathcal{M}(T!)$` by putting it in the denominator. (Copy over to fraction)
6. **te:** Balance with `$T!$` on top and consider what happens if `$T \to \infty$`. (Add `$T!$` on top. Limit appears in front)
7. **te:** This is the conjecture: It converges to a positive real number.

---

### Evidence
(**Title** Evidence)

1. **te:** Here is a plot of the fraction for our curve up to `$T=1000$`. Not clear yet. (Plot to `$T$` up to 1000, then increase.)
2. **st:** Does it converge? (doubtful) It seems bounded and well above 0 (assertive). (Plots all the way to `$10^9$` and slows down.)
3. **te:** We can plot the fraction for a few other curves, including the one that has only finitely many solutions. (Plot several curves in one graph, fade previous ones.)
4. **st:** Still not very convincing, but they do behave in a similar way. Oh, this last one has strange jumps (point to them).
5. **te:** Well spotted. That is due to a single pair of rational points. (Print the point coordinates)
   Here `$\mathcal{N}(T)$` jumps from 9 to 11 and then to 13.
6. **te:** The thing is, `$\mathcal{N}(T)$` grows actually slowly. The other terms grow super fast. (pause?)
7. **st:** And proving that conjecture wins you a million?
8. **te:** Yes. Oh, there’s one thing I forgot.
9. **st:** What?
10. **te:** We have to exclude some curves — those like this, they are singular. (Show family again but highlight singular curve.)
11. **st:** What is the graph for those curves? (Show graph up to `$T=1000$`.)
12. **st:** Logarithmic scale, please. (Changes to logarithmic scale) Agree, this converges clearly to `$0$`.
12. **te:** In general, we need to add one condition. (Show conjecture with `$\Delta \neq 0$`.)

---

(Rest is not done yet)

## Rank and Original Formulation

### The rank

1. **st:** How slow exactly?
2. **te:** That part we know very well, in fact.
3. **te:** Here is a theorem. (Show `$N(T) \sim \log(T)^{r/2}$`.)
4. **te:** This number `$r$` is called the *rank* of `$E$`.
5. (Show plots of three curves.)
6. **st:** We can replace `$N(T)^2$` with `$\log(T)$` in the conjecture.
7. **te:** Yep. (Show new conjecture.)
8. **st:** Are the graphs now more convincing?
9. (Show new graphs.)

---

### History

1. **te:** That is actually equivalent to the original first formulation of the conjecture found by two British mathematicians.
2. **te:** Bryan Birch and Peter Swinnerton-Dyer. (Show pictures.)
3. **te:** Swinnerton-Dyer was actually working in Cambridge on one of the first computers.
4. **te:** They ended up reformulating the conjecture using what we call *L-functions*, after André Weil suggested it. (Show Weil.)
5. **te:** Now the conjecture looks like this (show rank part).
6. **st:** What is `$L(E,s)$`?
7. **te:** An analytic function that encodes the number of points modulo `$U$` in a more convenient way.

---

### End

1. **st:** …and the two conjectures are equivalent.
2. **te:** Nah, not actually. The first one given here is better.
3. **te:** Our conjecture implies the modern formulation.
4. **te:** And even better — it implies the version of the Riemann hypothesis for the function `$L(E,s)$`.
5. **st:** Oh, two millions! (Walking out of the clouds again, `$\zeta$` and `$L$` together.)

---

Would you like me to render this as **HTML** (e.g. for a website or video script tool) or as **Markdown with math support** (e.g. for GitHub/Obsidian)?
