🧠 Core Idea Behind the Algorithm

We want the next bigger number, but the increase should be as small as possible.

To do that:

Step 1️⃣ – Find the "breaking point"

Go from right to left and find the first number that is smaller than the number next to it.

Why?
Because the right side is already in descending order — meaning it's the largest possible arrangement.

Step 2️⃣ – Swap with just bigger number

From the right side, find the smallest number bigger than the breaking point, and swap them.

This makes the number slightly bigger.

Step 3️⃣ – Reverse the right side

After swapping, the right side is still in descending order.

Reverse it to make it ascending — so the result is the smallest possible bigger number.

🔍 Detailed Example

Let’s take:

1 2 7 4 3 1
✅ Step 1: Find breaking point

From right:

3 > 1 ✔

4 > 3 ✔

7 > 4 ✔

2 < 7 ❗ ← breaking point = 2

So:

1 [2] 7 4 3 1
✅ Step 2: Find just bigger number than 2 (from right)

Numbers after 2: 7 4 3 1

Smallest number bigger than 2 is 3

Swap:

1 3 7 4 2 1
✅ Step 3: Reverse the right side

Right side after 3: 7 4 2 1

Reverse it:

1 3 1 2 4 7
🎯 Final Answer

Next permutation of:

1 2 7 4 3 1

is:

1 3 1 2 4 7
🚀 Why This Works

Right side is always decreasing.

We increase the number at the earliest possible position from the right.

Then we make the rest as small as possible.

That guarantees:

Next permutation = Smallest number greater than current one.
