class Solution
{
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node)
    {
        if (!node)
        {
            return NULL;
        }

        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> cloneMap;
        stack<UndirectedGraphNode*> nextToClone;

        cloneMap[node] = new UndirectedGraphNode(node->label);
        nextToClone.push(node);

        while (!nextToClone.empty())
        {
            UndirectedGraphNode* cloneMe = nextToClone.top();
            nextToClone.pop();
            UndirectedGraphNode* myClone = cloneMap[cloneMe];

            for (auto neighbor : cloneMe->neighbors)
            {
                auto neighborClone = cloneMap.find(neighbor);
                if (neighborClone != cloneMap.cend())
                {
                    myClone->neighbors.push_back((neighborClone->second));
                }
                else
                {
                    auto newClone = new UndirectedGraphNode(neighbor->label);
                    cloneMap[neighbor] = newClone;
                    myClone->neighbors.push_back(newClone);
                    nextToClone.push(neighbor);
                }
            }
        }

        return cloneMap[node];
    }
};
