select sum(a.count*b.count)
from Frequency a
join Frequency b
on a.term = b.term
where a.docid = "10080_txt_crude" and b.docid = "17035_txt_earn"
group by a.docid, b.docid;
