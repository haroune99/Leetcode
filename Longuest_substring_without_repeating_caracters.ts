function lengthOfLongestSubstring(s: string): number {
    const arr: number[] = new Array(s.length).fill(0);
    let temp: string[] = []
    temp.push(s[0])
    let count: number = 1
    for (let i=1; i<s.length; i++){
        if (!temp.includes(s[i])){
            count++
            temp.push(s[i])
        }
        else {
            arr[i] = count
            count = 1
            temp = []
            temp.push(s[i])
        }
    }
    
    return Math.max(...arr)

}
