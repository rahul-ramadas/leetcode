class MedianFinder
{
public:

    void addNum(int num)
    {
        if (m_leftElements.empty() && m_rightElements.empty())
        {
            m_leftElements.push(num);
            return;
        }

        if (!m_rightElements.empty() && (num > m_rightElements.top()))
        {
            m_rightElements.push(num);
        }
        else if (!m_leftElements.empty() && (num < m_leftElements.top()))
        {
            m_leftElements.push(num);
        }
        else
        {
            m_rightElements.push(num);
        }

        if (!m_leftElements.empty())
        {
            while ((m_leftElements.size() - 1) > m_rightElements.size())
            {
                m_rightElements.push(m_leftElements.top());
                m_leftElements.pop();
            }
        }

        while (m_leftElements.size() < m_rightElements.size())
        {
            m_leftElements.push(m_rightElements.top());
            m_rightElements.pop();
        }
    }

    double findMedian()
    {
        if (m_leftElements.size() == m_rightElements.size())
        {
            double left = m_leftElements.top();
            double right = m_rightElements.top();

            return (left + right) / 2.0;
        }
        else
        {
            return static_cast<double>(m_leftElements.top());
        }
    }

private:

    priority_queue<int, vector<int>, std::less<int>> m_leftElements;
    priority_queue<int, vector<int>, std::greater<int>> m_rightElements;
};
