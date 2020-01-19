func findAnagrams(s string, p string) []int {
	mm := [26]int{}
    var ret []int
    for i := range p {
        mm[p[i]-'a']++
    }
    var j int
    for i := range s {
        s1 := s[i]-'a'
        mm[s1]--
        for true {
            if mm[s1]>=0 {
                break
            }
            s2 := s[j]-'a'
            mm[s2]++
            j++
        }
        if i-j+1 == len(p) {
            ret = append(ret, j)
        }
    }
    return ret
}