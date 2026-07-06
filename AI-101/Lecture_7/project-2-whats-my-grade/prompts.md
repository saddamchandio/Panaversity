# Prompts used — What's My Grade, Really

## Initial prompt

> Here is my teacher's grading policy for CS-201, in plain text:
> - Quizzes 15% — five quizzes out of 10, drop the lowest one.
> - Assignments 10% — four assignments out of 100, all count.
> - Midterm 25% out of 100. Project 15% out of 100. Final 35% out of 100.
> - Special rule: if my final exam percentage is higher than my midterm
>   percentage, the midterm's 25% weight moves onto the final.
> My scores so far: quizzes 7,9,5,8,10 ; assignments 88,92,79,95 ;
> midterm 68 ; project 90 ; final not taken.
> Write a Python script that reads this from a JSON file and tells me my
> current grade on completed work.

## Improved prompt 1 — solve for the final

> Now add the second question: what exact percentage do I need on the final
> exam to finish with an A (85%)? Make sure the calculation correctly applies
> the replacement rule — if the required final beats my midterm, the midterm
> weight should move to the final and lower the bar.

## Improved prompt 2 — show the rule's impact

> When the replacement rule applies, also print what I *would* have needed
> without the rule, so I can see how much the rule helps me.

## Improved prompt 3 — keep it re-runnable

> Keep everything (policy + scores) in the JSON file so I can update it with
> new quiz and assignment marks through the term and just re-run the script.

## Verification prompt

> Before I trust the final-exam target, print each category percentage. I'll
> hand-check the quiz category: best 4 of (7,9,5,8,10) is 34/40 = 85%. If the
> script also says 85.00% for quizzes, I'll trust the rest.
