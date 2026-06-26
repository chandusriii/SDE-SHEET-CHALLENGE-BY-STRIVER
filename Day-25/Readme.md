# 📚 Day 24 - Stack & Queue

Welcome to **Day 24** of my **Striver's SDE Sheet Challenge**! 🚀

Today, I solved fundamental Stack-based problems that strengthen understanding of stacks, recursion, and monotonic stack techniques.

---

## ✅ Problems Solved

### 1. Balanced Parentheses
- **Concept:** Stack
- **Difficulty:** Easy

**Approach:**
- Traverse the string character by character.
- Push every opening bracket onto the stack.
- For every closing bracket, check whether it matches the stack's top.
- If all brackets are matched and the stack is empty at the end, the expression is balanced.

**Time Complexity:** `O(N)`

**Space Complexity:** `O(N)`

---

### 2. Next Greater Element
- **Concept:** Monotonic Stack
- **Difficulty:** Easy

**Approach:**
- Traverse the array from right to left.
- Maintain a decreasing stack.
- Remove all smaller or equal elements.
- The remaining top element is the next greater element.
- Push the current element onto the stack.

**Time Complexity:** `O(N)`

**Space Complexity:** `O(N)`

---

### 3. Sort a Stack
- **Concept:** Recursion + Stack
- **Difficulty:** Medium

**Approach:**
- Recursively remove all elements from the stack.
- Insert each element back into its correct position using another recursive helper function.
- No additional data structures or sorting algorithms are used.

**Time Complexity:** `O(N²)`

**Space Complexity:** `O(N)`

---

## 📖 Key Concepts Learned

- Stack implementation
- Parentheses validation
- Monotonic Stack
- Next Greater Element
- Recursion with Stack
- Recursive insertion
- Stack sorting without loops
- Time and Space Complexity Analysis

---

## 🚀 Challenge Progress

- ✅ Topic: Stack & Queue
- ✅ Problems Solved: **3**
- ✅ Learned stack operations, monotonic stack techniques, recursive stack sorting, and interview-standard approaches for stack-based problems.

---

### ⭐ Repository

If you find this repository helpful, consider giving it a **⭐ Star** and follow my journey through **Striver's SDE Sheet Challenge**.

**Happy Coding! 🚀**
