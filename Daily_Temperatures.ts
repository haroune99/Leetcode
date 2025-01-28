function dailyTemperatures(temperatures: number[]): number[] {
    let answer: number[] = [];
    for(let i=0; i<temperatures.length; i++){
        for(let j=i+1;j<temperatures.length; j++){
            if (temperatures[j]>temperatures[i]) {
                answer.push(j-i);
                break;
            }
            else {
                if (j != (temperatures.length-1)){
                    continue;
                }
                answer.push(0)
            }
        }
    }
    answer.push(0)
    return answer
};
