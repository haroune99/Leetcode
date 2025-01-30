function lengthOfLongestSubstring(s: string): number {
    const arr: number[] = new Array(s.length).fill(0);
    let temp: string[] = [];
    let count: number = 0;
    let maxCount: number = 0;
    
    if (s.length === 0) {
        return 0;
    }
    if (s.length === 1) {
        return 1;
    }

    for (let i = 0, j = 0; i < s.length; i++) {
        while (temp.includes(s[i])) {
            temp.shift(); 
            count--;
        }
        temp.push(s[i]);
        count++;
        arr[i] = count;
        maxCount = Math.max(maxCount, count);
    }
    
    return maxCount;
}

