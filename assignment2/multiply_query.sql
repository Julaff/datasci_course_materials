select a.row_num, b.col_num, sum(a.value * b.value)
from a join b on b.row_num = a.col_num
group by a.row_num, b.col_num;
