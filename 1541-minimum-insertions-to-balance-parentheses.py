# leetcode-dsa-solutions
My journey learning Data Structures and Algorithms with Python.

🎯 Goals
Build problem-solving and logical thinking skills.
Understand solutions instead of memorizing code.
Practice LeetCode problems consistently.

1541. Minimum Insertions to Balance a Parentheses String,Greedy,Strings	Medium

Solution below:
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_brackets = 0
        i = 0
        while i < len(s):
            if s[i] == '(' :
                open_brackets += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1
                if open_brackets > 0:
                    open_brackets -= 1

                else:
                    insertions += 1
            i += 1
        insertions += open_brackets * 2
        return insertions   


💡 My Approach

Intuition

Imagine that every opening bracket ( needs two closing brackets )).

We count how many brackets we need to insert to make every opening bracket match its required two closing brackets.

Approach

When we see (, increase open_brackets because we have a new opening bracket to match.

When we see ), check whether the next character is also ).

If yes, we have the required pair )).

If no, add one ) because we need to complete the pair.

If there is an opening bracket available, match it. Otherwise, insert a ( and count one insertion.

At the end, each unmatched ( needs two ) characters, so add open_brackets * 2.

Complexity

Time: O(n) — We go through the string once.

Space: O(1) — We use only a few variables.
Language: Python 3

More solutions coming soon!
