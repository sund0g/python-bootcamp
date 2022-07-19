Rounding becomes an issue when the next digit after the last to be kept is a 5. Computers and most people round up if the following digit is a 5 (this is the 4/5 rounding rule: 4 or less, leave alone; 5 or more, round up).

Example: 34.65 to 3 sig fig rounds to 34.7

This approach works well for most cases.

Surveyors, on the other hand, use an even rounding rule when the next digit is a 5;

if the last digit to be kept is even, it is left as is,
if the last digit to be kept is odd, it is increased to the next even.
Examples:

        34.65 to 3 sig fig rounds to 34.6

        18.215 to 4 sig fig rounds to 18.22

If you follow the surveyor’s rule, what about numbers which follow the 5?

For example how would you round 12.5496 to 2 sig fig?

Is .5496 greater than .5 so in this case we’d round to 13?

Remember what sig fig are: the digits of which we’re certain plus an estimate. The 5 isn’t a sig fig - the preceding digit is and that’s an estimate. We’re using the 5 to refine that estimate. The 5 is 10 times less significant than the estimate, the following 4 is 100 times less significant, and so on. Basically, anything after the 5 is garbage, noise, and can be ignored: key only on the 5.

Therefore, 12.5496 to 2 sig fig would round to 12.

So why do surveyors use this rule? Well, for many non-digital measuring devices, the smallest division can usually be estimated to 1/2. That means there’s a 50/50 chance of estimating incorrectly. If we always rounded up when encountering a 5 (the half-division), then the rounding would always be biased in one direction. By using the even rounding rule, sometimes we round up, sometimes down; in the end it evens out (we’re really quite a clever bunch).