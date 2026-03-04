📈 Best Time to Buy and Sell Stock
📝 Problem Statement

Given an array prices where:

prices[i] represents the price of a stock on the i-th day

You must buy before you sell

You can complete at most one transaction

Return the maximum profit you can achieve.
If no profit is possible, return 0.

📌 Examples
Example 1
Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6).
Profit = 6 − 1 = 5

Example 2
Input: prices = [7,6,4,3,1]
Output: 0

Explanation:
No profitable transaction is possible, so return 0.

🚀 Approach
🔎 Key Observations

We must buy before selling

We want to:

Buy at the lowest possible price

Sell at the highest possible price after buying

Only one transaction is allowed

💡 Strategy

Track the Minimum Price

Iterate through the array.

Keep updating the lowest price seen so far.

Calculate Potential Profit

For each day:

Calculate current_price - minimum_price_so_far

This gives the profit if sold on that day.

Track Maximum Profit

Maintain a variable to store the maximum profit found so far.

Update it whenever a larger profit is found.

Edge Case

If prices continuously decrease:

No profit can be made.

Return 0.

🧠 Why This Works

We ensure buying happens before selling.

We only scan the array once.

Efficient and avoids unnecessary nested loops.

⏱ Time & Space Complexity

Time Complexity: O(n)

Space Complexity: O(1)

If you'd like, I can also provide:

Brute-force approach explanation

Optimized intuition breakdown

Flowchart-style explanation

Interview-ready explanation version 🚀
