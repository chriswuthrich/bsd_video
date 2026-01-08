
# Script for the BSD Video

**Author:** cw

---

## Introduction

The purpose of this part is to introduce the two characters and to delve into
the thought bubble.
The title only appears in the middle.

1. **st + te** centred, walking through a natural background towards the
   lower-left corner.
2. **st:** "I have heard about the Riemann hypothesis." 
   Thought bubble with `$\zeta(s)$`.
   "You are a number theorist. Are you working on this?"
3. **te:** "Not directly. My research concerns another important conjecture,
   also worth a million dollars." 
   In the bubble `$\zeta(s)$` is kicked out for an elliptic curve, the bubble
   grows slowly. A bag of gold coins could also appear together with the
   typical money/till sound. 
4. **st:** "Which conjecture?"
5. **te:** "The Birch and Swinnerton-Dyer conjecture."
   The **Title** The Birch and Swinnerton-Dyer conjecture
   appears within the growing bubble.
6. **st:** "Can you explain?"
7. **te:** "Sure." 
8. Bubble increases to take over the complete background. 
   The two characters have reached the lower left corner; they stay in (above)
   the bubble until the whole screen is in the bubble. 

---

## Elliptic curves
(**Title** Elliptic curves)

Now we learn what an elliptic curve as a picture.

1. **te:** "It deals with equations like, `$y^2 = x^3 - 4x + 1$`, called
   elliptic curves"
   Reads "y squared equals x cubed minus 4 x plus 1", small pauses before and
   after.
   The equation appears centered.
2. **st:** "What do they look like?"
3. **te:** "Here is a picture." 
   Equation moves up left, curve appears.
4. **st:** "What are other examples?"
5. **te:** "We need, y squared equals x cubed plus some integer times x plus
   another integer."
   Equation and picture show other curves with coefficients framed.
6. **te:** "Some are formed of two pieces some only are only one piece"
   In the picture the curve goes through a family of curves with one piece
   detaching and then back.
7. **st:** "Are they all symmetric?"
   The picture is back to the original curve and arrows appear that indicate
   the symmetry.
8. **te:** "Yes, as y only appears as an even power".
   The equation highlights this.

---
   
## Rational Points 
(**Title** Rational points)

Here we draw the focus on points with rational coordinates. This involves also
looking at the point infinitely far away.

1. **st:** "What do you study about them?"
2. **te:** "I count solutions to the equation with both x and y rational."
   `$x,y \in \mathbb{Q}$` appears.
3. **st:** "Hmm" (thinks), "like when x is zero then y is 1." (little gap)
   "Or y is minus 1."
   These two points highlight with sparks around them.
4. **te:** "Yep. I chose an example with a lot of solutions. Some lie outside
   the screen. Some have very complicated coordinates."
   Points are highlighted successively, including one really complicated
   example.
5. **st:** reacts surprised to the large numbers. (?)
6. x=X/Z and y=Y/Z appear.
   **te:** "We can write little x equals big X over big Z and  little y equals
   big Y over big Z. 
   We can take big Z to be the least common denominator."
   The equation moves up and y us substituted by Y/Z etc.
7. **te:** "Multiply by Z cubed".
   The equation becomes `$Y^2Z = X^3 - 4XZ^2 + Z^3$`.
8. **st:** "I know this is a projective curve."
9. **te:** "Indeed. We can now study integer solutions big X, big Y, big Z to
   this equation instead of rational little x, little y."
10. **te:** "But if we do, do we get extra solutions — like when Z is
   negative?  We need to identify solutions when they are scalar multiples of each other. 
   (X,Y,Z) ~ (-X,-Y,-Z) ~ (2X,2Y,2Z) etc appears.
11. **te:** "And we have accidentally added a new point — the one with Z equals
   zero, X equals 0, and Y equals 1."
12. **te:** "We should visualize it as a point infinitely far away."
   "It is at the horizon."
   This turn to 3D scene where the usual plane flips down.
   (This graphical part will need improvement.)
13. **st:** "Wow." (surprise) 
   (The character could either stay in the 2D plane and be lifted down and
   become "flat". Or We could leave them in the front and the are just
   surprised that the ground is taken underneath their feet.
14. **te:** "No worries. Now we see the unique point at infinity and — look —
   the horizon is a tangent to our curve."
   The point at infinity gets pointed out. Then we flip back to the 2D world.


---


## Counting rational points
(**Title** Counting rational points)

The main point is to define the quantity N(T) and to plot a graph of it.

1. **te:** "The conjecture is about counting rational solutions."
2. **st:** "There are only finitely many?" (surprised, not believing it)
3. **te:** "No!" (reassuring) "Well, for some curves like y squared equals x
   cubed minus 4 x minus 2" (the minus 2 should be emphasised) "there are only
   four points." 
   The equation `$y^2 = x^3 - 4x - 2$` appears and that curve is drawn and all 
   four points are highlighted.
4. **te:** "But for our first example, there are infinitely many solutions."
5. **te:** "We count them by the size of the integers involved."
6. **te:** "For instance, there are 15 solutions with big X, big Y and big Z
   all smaller than 10..."
   The condition `|X|, |Y|, |Z| < 10` appears with the list of all 15 points.
   They are quickly highlighted.
7. **te:** "... and 27 smaller than 100 and even more smaller than 1000."
   Lists with more points appear.
8. **te:** We call, N of T, the number of points with integer coordinates below
   T."
   The definition of `$\mathcal{N}(T)$` appears on top.
9. **st:** "I see, these are the first solutions we would find if we search for
   them with a computer."
10. **te:** "Yep. Searching in a box, I'd call it."
11. **te:** "This gives a function with a graph that looks like a staircase."
   Graph plots increasingly.

---

## Counting points modulo
(**Title** Counting points modulo)

This introduces M(T) and shows a bar chart picture of that function.

1. **te:** "This counting will be compared to counting modulo."
   The equality sign is replaced by a congruence sign and it moves down.
2. **te:** "We look for integers such that both sides have the same remainder
   when dividing by — say — 10."
   The points appear scattered over the "plane" modulo 10.
3. **st:** "You just solve, y square equals x cubed minus 4 x plus 1, 
   modulo 10 ?"
4. **te:** "Ehmm", (embarrassed) "yes, but I shouldn't work with small x, y
   but with big X Y Z to get what is at infinity."
   The equation changes to Y^2...
5. **te:** "I still have to remember to identify equal points when scaling.
   One can scale with 3, 7 or 9; the invertibles modulo 10."
   The scaling by 3 appears on the left.
6. **te:** "Strangely, there is more than one. In total we get 27 solutions
   modulo 10, of which 11 are at infinity."
   The additional points appear and all change to triples.
7. **te:** "We define M of U as the number of solutions modulo an integer U."     
   The definition of `$\mathcal{M}(U)$` appears
8. **te:** "As U increases, the number of solutions modulo U grows."
   Bar chart of values of `$\mathcal{M}(U)$`
9. **st:** "But not continuously at all."
10. **st:** Common, what is the conjecture now?"

---

## The conjecture
(**Title** The conjecture)

We put the two together and present evidence for the conjecture.

1. **te:** "Recall the functions N and M."" 
   Their defintions appear on the right half.
2. **te:** "Pick T large and set U to be T factorial."
   Shows up and U transforms to T!
3. **st:** "If T is biiig, T factorial is huuuuge."
4. **te:** "Put N of T on top of a fraction, and square it."
   Copy over to fraction and add square to the formula.
5. **te:** "We compare it to M of T factorial by putting that in the
   denominator."
   Copy over to denominator of the fraction.
6. **te:** "Finally, balance it with T factorial on top. Consider what
   happens if T goes to infinity."
   Adds `$T!$` on top and the limit appears in front.
7. **te:** "This is the conjecture: It converges to a positive real number."

8. **te:** "Here is a plot of that fraction for our curve up to T equal 1000."      
   Plot to T up to 1000 appears and starts increasing.
9. **st:** "Not clear yet. Does it converge?" (doubtful) 
   "It seems bounded and well above 0." (assertive).
   Plots all the way to 10^9 and slows down.
10. **te:** "We can plot the fraction for a few other curves, including the one
   that has only finitely many solutions."
   Plot several curves in one graph, fade previous ones.
11. **st:** "Still not very convincing, but they do behave in a similar way.
   Oh, this last one has strange jumps"
   An arrow pointing to a jump appears.
12. **te:** "Well spotted. That is due to a single pair of rational points."
   Print the point coordinates.
   "Here N of T jumps from 9 to 11 and then to 13."
13. **te:** "The thing is, N of T grows slowly. The other terms grow super
   fast." (pause?)
14. **st:** "And proving that conjecture wins you a million?"
15. **te:** "Yes. Oh, there’s one thing I forgot." (appologetic)
16. **st:** "What?"
17. **te:** "We have to exclude some curves. Remember what they can look like.
   This one here which crosses itself is no good."
   Shows the family again but highlight singular curve.
18. **te:** "The equation factors with a square on the right. This happens
   when 4 A cubed plus 27 B square is zero. Those we have to exclude."
   The formula for the discriminant appears on the top left.
19. **st:** "What is the graph for those curves?"
   Show graph up to `$T=1000$` going down quickly.
20. **st:** "Logarithmic scale, please."
   Changes to logarithmic scale.
21. **st:** " Agree, this converges clearly to zero".
22. **te:** "If we add this one condition, we get the correct statement of the
   conjecture".
   Show conjecture again with extra condition at the start. (Money bag again?)


(Rest is not done yet coded)
 
26. **st:** "Is it known what the limit is?"
27. **te:** "Yes, but I am not sure you want to see the huge formula."
    The formula appears, shy hidden and goes away before one can read it.

---


## Origin
(**Title** Origin)

1. **st:** "What was the name of the conjecture again?"
2. **te:** "It is named after Bryan Birch and Peter Swinnerton-Dyer. Here a 
   picture from 2011. Swinnerton-Dyer on the right passed away in 2018."
   Show picture of the two.
3. **st:** "How old is the conjecture?"
4. **te:** "They discovered it in the fifties. At the time Swinnerton-Dyer was 
   working on one of the first computers, so he was really one of the first
   programmers. It was calculated a bit differently than what I showed you."
   The bubble slowly shrinks back, we could add a picture of the computer in
   question.
5. **te:** "The two met André Weil who pointed them to L functions. The modern
   version of the conjecture is in terms of that function."
   Picture of Weil?
6. **st:** "What are L functions? What is the new formulation."
   L(E,s) appears in the bubble.
7. **te:** "The L function of an elliptic curve packages the point count modulo
   U in a better way. The new conjecture says the growth of N of T is encoded
   in the way this L function behaves at s equals 1"
   Conjecture with ord appears.
8. **st:** "…and the two conjectures are equivalent?"
9. **te:** "Nah, not actually. The conjecture that I explained implies the
   modern formulation. And even better — it implies the version of the Riemann
   hypothesis for the L function."
10. **st:** "Oh, two millions!"
   Now both zeta L and the elliptic curve are left in the bubble that vanishes.
   Two bags of gold and two money sounds.

---

Thanks and credits.

---
