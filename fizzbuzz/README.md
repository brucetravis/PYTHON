FIZZBUZZ
Print numbers from 1 to 100
for multiples of 3, print “Fizz”
for 5 print “Buzz”, 
and for both, print “FizzBuzz”.


# NOTES
The most restrictive condition must be checked first to avoid missing out on special cases.

Analogy: Security Check at an Event
Imagine you’re organizing an event with three types of guests:

VIP guests (have both an invitation & an access card).
Guests with only an invitation.
Guests with only an access card.
Regular people without any pass.
If you were checking people at the entrance, which order would you check them in?

👉 You should check for VIPs first (since they meet both conditions: invitation and access card).
👉 Then, check for guests with only an invitation.
👉 Then, check for guests with only an access card.
👉 Lastly, if someone has none of the above, you can turn them away.

If you checked for invitation first, you’d let VIPs through as just "invited guests," and they wouldn’t get their VIP treatment. The most restrictive condition must be checked first to avoid missing out on special cases.

Applying This to Code (FizzBuzz Example)
Now, let’s map this analogy to FizzBuzz:

VIP guests = Numbers divisible by both 3 and 5 (should be "FizzBuzz").
Guests with only an invitation = Numbers divisible by 3 (should be "Fizz").
Guests with only an access card = Numbers divisible by 5 (should be "Buzz").
Regular people = Numbers that aren’t divisible by 3 or 5 (should be printed as they are).
If you check num % 3 == 0 first, the number 15 will be treated as just a "Fizz" guest, even though it should be "FizzBuzz".

That’s why we check num % 3 == 0 and num % 5 == 0 first, so VIPs get their proper "FizzBuzz" treatment.


# NOTE
Does the Order (5 then 3) Make a Difference?
Logically, no → It still produces the correct output.
Performance-wise, no big difference → Both are efficient.
Preference-wise, YES → If it feels more natural to think multiples of 5 first, then go for it!
Key Takeaway
The most important rule is that FizzBuzz comes first to avoid double-printing.
After that, whether you check 5 before 3 or 3 before 5 is just a preference.

Great thinking! Do you want to try tweaking another logic-based problem next? 😊

