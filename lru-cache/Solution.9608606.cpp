class LRUCache
{
public:

    LRUCache(int capacity)
        : m_capacity(capacity)
    {
    }

    int get(int key)
    {
        auto it = m_values.find(key);
        if (it == m_values.end())
        {
            return -1;
        }

        touch(it);
        return it->second->second;
    }

    void set(int key, int value)
    {
        if (m_capacity == 0)
        {
            return;
        }

        auto it = m_values.find(key);

        if (it == m_values.end())
        {
            if (m_capacity == m_ageList.size())
            {
                removeOldest();
                add(key, value);
            }
            else
            {
                add(key, value);
            }
        }
        else
        {
            touch(it);
            it->second->second = value;
        }
    }

private:

    void add(int key, int value)
    {
        m_ageList.emplace_front(make_pair(key, value));
        m_values[key] = m_ageList.begin();
    }

    void touch(unordered_map<int, list<pair<int, int>>::iterator>::iterator elem)
    {
        auto entry = *(elem->second);
        m_ageList.erase(elem->second);
        m_ageList.emplace_front(std::move(entry));
        elem->second = m_ageList.begin();
    }

    void removeOldest()
    {
        m_values.erase(m_ageList.back().first);
        m_ageList.pop_back();
    }

    list<pair<int, int>> m_ageList;
    unordered_map<int, list<pair<int, int>>::iterator> m_values;
    int m_capacity;
};
