/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

import java.util.HashMap;

class Solution {
    public Node cloneGraph(Node node) {

        var memo = new HashMap<Integer, Node>();
        return dfs(node, memo);
    }

    private Node dfs(Node u, HashMap<Integer, Node> memo) {
        if (u == null) {
            return null;
        }

        if (memo.containsKey(u.val)) {
            return memo.get(u.val);
        }

        var newNode = new Node(u.val);
        memo.put(u.val, newNode);

        for (var v : u.neighbors) {
            newNode.neighbors.add(dfs(v, memo));
        }
        return newNode;
    }
}