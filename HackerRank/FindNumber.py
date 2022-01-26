
check if k is in the array if its there return "YESS" if its not there preturn "NO"




function findNumber(arr, k) {
    // Write your code here
    let count=arr.length;
    for(var i=0;i<count;i++)
    {
        if(arr[i]===k){return "YES";}
    }
    return "NO";     

}
