class Solution
{
private:

    void buildPaths(vector<string>& path, unordered_map<string, int>& distanceFromEnd, vector<vector<string>>& results)
    {
        string word = path.back();
        int currentDistance = distanceFromEnd[word];
        if (currentDistance == 0)
        {
            results.push_back(path);
            return;
        }

        int nextDistance = currentDistance - 1;

        for (size_t j = 0; j < word.length(); ++j)
        {
            for (int k = 1; k <= 26; ++k)
            {
                word[j] = (word[j] + 1 - 'a') % 26 + 'a';
                if (k == 26)
                {
                    continue;
                }

                auto it = distanceFromEnd.find(word);
                if (it == distanceFromEnd.end())
                {
                    continue;
                }

                if (it->second != nextDistance)
                {
                    continue;
                }

                path.push_back(word);
                buildPaths(path, distanceFromEnd, results);
                path.pop_back();
            }
        }
    }

public:
    vector<vector<string>> findLadders(string start, string end, unordered_set<string> &dict)
    {
        unordered_map<string, int> distanceFromEnd;
        distanceFromEnd[end] = 0;
        queue<string> frontier({ end });
        dict.insert(end);
        dict.insert(start);

        while (!frontier.empty() && distanceFromEnd.find(start) == distanceFromEnd.end())
        {
            size_t frontierSize = frontier.size();

            while (frontierSize--)
            {
                string word = frontier.front();
                frontier.pop();
                int newDistance = distanceFromEnd[word] + 1;

                for (size_t j = 0; j < word.length(); ++j)
                {
                    for (int k = 1; k <= 26; ++k)
                    {
                        word[j] = (word[j] + 1 - 'a') % 26 + 'a';
                        if (k == 26)
                        {
                            continue;
                        }

                        if (dict.find(word) == dict.end())
                        {
                            continue;
                        }

                        if (distanceFromEnd.find(word) != distanceFromEnd.end())
                        {
                            continue;
                        }

                        distanceFromEnd[word] = newDistance;
                        frontier.push(word);
                    }
                }
            }
        }

        vector<vector<string>> results;

        if (distanceFromEnd.find(start) == distanceFromEnd.end())
        {
            return results;
        }

        vector<string> path({ start });
        buildPaths(path, distanceFromEnd, results);

        return results;
    }
};
