/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:

    bool intersects(const Interval& a, const Interval& b)
    {
        if (a.start <= b.start && a.end >= b.start)
        {
            return true;
        }
        else if (b.start <= a.start && b.end >= a.start)
        {
            return true;
        }
        return false;
    }
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        
        if (intervals.empty())
        {
            return vector<Interval>{ newInterval };
        }
        
        int eraseStart;
        int begin = 0;
        int end = (int)intervals.size();
        bool foundOne = false;
        
        while (begin < end)
        {
            int mid = begin + (end - begin) / 2;
            
            Interval& trial = intervals[mid];
            if (intersects(newInterval, trial))
            {
                foundOne = true;
                eraseStart = mid;
                end = mid;
            }
            else if (trial.start > newInterval.end)
            {
                if (!foundOne)
                {
                    eraseStart = mid;
                }
                end = mid;
            }
            else // if (trial.end < newInterval.start)
            {
                if (!foundOne)
                {
                    eraseStart = mid;
                }
                begin = mid + 1;
            }
        }
        
        if (!foundOne)
        {
            if (intervals[eraseStart].start > newInterval.end)
            {
                intervals.insert(intervals.begin() + eraseStart, newInterval);
                return intervals;
            }
            else
            {
                intervals.insert(intervals.begin() + eraseStart + 1, newInterval);
                return intervals;
            }
        }
        
        int eraseEnd = eraseStart;
        begin = eraseEnd + 1;
        end = (int)intervals.size();
        
        while (begin < end)
        {
            int mid = begin + (end - begin) / 2;
            
            Interval& trial = intervals[mid];
            if (intersects(newInterval, trial))
            {
                eraseEnd = mid;
                begin = mid + 1;
            }
            else // if (trial.start > newInterval.end)
            {
                end = mid;
            }
        }
        
        int rangeStart = min(intervals[eraseStart].start, newInterval.start);
        int rangeEnd = max(intervals[eraseEnd].end, newInterval.end);

        intervals[eraseStart].start = rangeStart;
        intervals[eraseStart].end = rangeEnd;
        ++eraseStart;
        ++eraseEnd;
        
        intervals.erase(intervals.begin() + eraseStart, intervals.begin() + eraseEnd);
        return intervals;
    }
};