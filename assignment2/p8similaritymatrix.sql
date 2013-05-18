select d1.docid, d2.docid
from Frequency as d1, Frequency as d2
where d1.term = d2.term
group by d1.docid, d2.docid
;

