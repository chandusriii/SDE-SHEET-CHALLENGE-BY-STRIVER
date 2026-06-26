# Day 26 – Stack & Queue

## 📌 Topic: Cache Design (LRU & LFU Cache)

Today I solved two advanced data structure design problems focused on implementing efficient cache systems. Both problems required combining **Hash Maps** and **Doubly Linked Lists** to achieve **O(1)** average time complexity for cache operations.

---

## ✅ Problems Solved

### 1. LRU Cache

**Problem Statement:**
Design an **LRU (Least Recently Used) Cache** that supports `get()` and `put()` operations in **O(1)** time. When the cache reaches its capacity, remove the least recently used item before inserting a new one.

#### Key Concepts
- Hash Map
- Doubly Linked List
- Cache Eviction Policy
- Data Structure Design

#### Approach
- Use a hash map to map keys to their corresponding nodes.
- Maintain a doubly linked list to store cache entries based on recent usage.
- Move accessed or updated nodes to the most recently used position.
- Remove the least recently used node when the cache exceeds its capacity.

#### Time Complexity
- **get()** → `O(1)`
- **put()** → `O(1)`

#### Space Complexity
- **O(capacity)**

---

### 2. LFU Cache

**Problem Statement:**
Design an **LFU (Least Frequently Used) Cache** that supports `get()` and `put()` operations in **O(1)** average time. When the cache is full, remove the least frequently used item. If multiple items have the same frequency, remove the least recently used among them.

#### Key Concepts
- Hash Map
- Frequency Map
- Doubly Linked List
- Cache Eviction Policy
- Constant-Time Data Structure Design

#### Approach
- Store key-node mappings in a hash map.
- Maintain the access frequency of each node.
- Use separate doubly linked lists for each frequency.
- Track the minimum frequency currently present in the cache.
- On every access or update, move the node to the next higher frequency list.
- Evict the least recently used node from the minimum frequency list when the cache is full.

#### Time Complexity
- **get()** → `O(1)` Average
- **put()** → `O(1)` Average

#### Space Complexity
- **O(capacity)**

---

## 💡 Key Learnings

- Learned the implementation of **LRU** and **LFU** cache eviction strategies.
- Strengthened understanding of combining **Hash Maps** and **Doubly Linked Lists** for efficient data structures.
- Understood how frequency tracking and recency tracking work together in cache design.
- Improved skills in designing real-world system components with **O(1)** average operations.
- Gained insights into cache implementations commonly used in operating systems, databases, browsers, and distributed applications.

---

## 🚀 Day 26 Summary

- ✅ Solved **2 Advanced Design Problems**
- 📚 Topic Covered: **Stack & Queue – Cache Design**
- 💻 Mastered **LRU Cache** and **LFU Cache** implementations.
- 🎯 Continued progressing through the **Striver SDE Sheet Challenge** while strengthening system design and advanced data structure concepts.

---
