select docid, sum(count)
from Frequency
where term in ("washington", "taxes", "treasury")
group by docid
order by count;
