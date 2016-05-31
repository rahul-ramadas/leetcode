class MedianFinder
{
public:

    void addNum(int num)
    {
        m_leftElements.push(num);
        m_rightElements.push(m_leftElements.top());
        m_leftElements.pop();
        if (m_leftElements.size() < m_rightElements.size())
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
