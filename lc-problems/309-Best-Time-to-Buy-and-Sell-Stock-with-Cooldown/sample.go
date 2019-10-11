import (
    "math"
)

type M struct{
	stat string
	index int
}



func maxProfit(prices []int) int {
    if len(prices) == 0{
        return 0
    }
    mem := make(map[M]float64)
    return int(helper(prices,"b",0,mem))
	
}

func helper(prices []int,s string,i int,mem map[M]float64) float64{
	
    var node M
	node.stat = s
	node.index = i
	v,ok := mem[node]
	if ok{
		return v
	}
    if i >= len(prices){
		return 0
	}
	
	if s == "b"{
		mem[node] = math.Max(helper(prices,"b",i+1,mem),helper(prices,"s",i+1,mem))
	}else if s == "s"{
		p := prices[i] - prices[i-1]
        mem[node] = math.Max(helper(prices,"s",i+1,mem),helper(prices,"b",i+2,mem)) + float64(p)
	}
	return mem[node]
}