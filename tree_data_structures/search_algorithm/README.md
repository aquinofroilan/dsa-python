| **Traversal** | **Implementation Style**     | **Core Data Structure**   | **Supports Early Termination** | **Handles Cycles (Graph)**  | **Common in**         |
| ------------- | ---------------------------- | ------------------------- | ------------------------------ | --------------------------- | --------------------- |
| **BFS**       | Iterative                    | `Queue` (usually `deque`) | ✅ Yes                          | ✅ Yes (with visited set)    | Graphs, trees         |
| **DFS**       | Recursive (Pre/In/Post)      | Call stack (implicit)     | ✅ Yes                          | ⚠️ No\* (needs visited set) | Binary trees, parsing |
| **DFS**       | Iterative                    | `Stack` (manual)          | ✅ Yes                          | ✅ Yes (with visited set)    | Graphs, mazes         |
| **BFS**       | Recursive (uncommon)         | Recursive queue layering  | ⚠️ Rare and clumsy             | ⚠️ Not practical            | Theoretical only      |
| **DFS**       | Tail-recursive (optimized)\* | Call stack                | ✅ Yes                          | ⚠️ With care                | Functional languages  |
