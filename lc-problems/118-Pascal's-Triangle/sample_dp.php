/**
* @param Integer $numRows
* @return Integer[][]
*/
function generate($numRows) {
  $res=[];
   for($i=0;$i<$numRows;$i++){
       for($j=0;$j<=$i;++$j){
           if($i==0 && $j==0) $res[0][0]=1;
           else $res[$i][$j]=$res[$i-1][$j-1]+$res[$i-1][$j];
           
       }
   }
   return $res;
}