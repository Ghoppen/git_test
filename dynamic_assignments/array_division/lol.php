<?php
$pos1 = -1;
$pos2 = -1;

function calculateConsecutiveSums($numbers)
{
    $summed_members = array_fill(0, count($numbers), 0);
    $sum = 0;
    for($i = 0; $i < count($numbers); $i++)
    {
        $sum += $numbers[$i];
        $summed_members[$i] = $sum;
    }
    
    return $summed_members;
}

function addArrayMembers($numbers){

    $sum = 0;
    for ($i = 0; $i < count($numbers); $i++)
    {
        $sum += $numbers[$i];
    }
    return $sum;
}

function equiSumUtil($arr)
{
    global $pos2, $pos1;

    $array_size = count($arr);
    $total_sum = addArrayMembers($arr);
    $prefix_sum = calculateConsecutiveSums($arr);
    $sufix_sum = calculateConsecutiveSums(array_reverse($arr));  
    print_r($prefix_sum);
    print_r($sufix_sum);


    $i = 0; 
    $j = $array_size - 1;
    $third_of_total_sum = $total_sum / 3;
    while ($i < $j - 1)
    {
        print "pos1: $i \n";
        print "pos2: $j \n";

        if ($prefix_sum[$i] == $third_of_total_sum)
        {
            $pos1 = $i;
        }

        if ($sufix_sum[$j] == $third_of_total_sum)
        {
            $pos2 = $j;
        }

        if ($pos1 != -1 && $pos2 != -1)
        {
            if ($sufix_sum[$pos1 + 1] - $sufix_sum[$pos2] == $third_of_total_sum)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        if ($prefix_sum[$i] < $sufix_sum[$j])
        {
            $i++;
        }
        else
        {
            $j--;
        }
    }
    return false;
}

function equiSum($arr)
{
    global $pos2,$pos1;
    $ans = equiSumUtil($arr);
    if ($ans)
    {

        print("First Segment : ");
        for ($i = 0; $i <= $pos1; $i++)
        {
            print($arr[$i] . " ");
        }

        print("\n");

        print("Second Segment : ");
        for ($i = $pos1 + 1; $i < $pos2; $i++)
        {
            print($arr[$i] . " ");
        }

        print("\n");

        print("Third Segment : ");
        for ($i = $pos2; $i < count($arr); $i++)
        {
            print($arr[$i] . " ");
        }

        print("\n");
    }
    else
    {
        print("Array cannot be divided into three equal sum segments");
    }
}

$arr = array(1, 3, 6, 2, 7, 1, 2, 8 );
equiSum($arr);
?>