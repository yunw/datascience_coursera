# http://www.sqlite.org/sqlite.html
# http://www.blogjava.net/wxqxs/archive/2009/04/15/265712.html

#.mode column
# select * from freqency

# problem1: a
SELECT count(*) FROM Frequency WHERE docid = "10398_txt_earn";

# problem1: b
SELECT count(term) FROM Frequency WHERE docid = "10398_txt_earn" and count = 1;

# problem1c:

sqlite> .output p1c_union.txt
sqlite> SELECT count(term) from(
   ...> SELECT term FROM Frequency WHERE docid = "10398_txt_earn" and count = 1
   ...> UNION
   ...> SELECT term FROM Frequency WHERE docid="925_txt_trade" and count = 1);


#p1e:
sqlite> .output p1d_count.txt
sqlite> select count(docid) from Frequency where term = "parliament"
   ...> ;

qlite> .output p1e_bigDoc.txt
sqlite> select count(docid) from (
   ...> select docid from Frequency group by docid having count(term) > 300
   ...> );
## didnt take count in the term frequences

sqlite> select count(docid) from (
   ...> select docid from Frequency group by docid having sum(count) > 300
   ...> );


#p1f:
sqlite> select count(docid) from (
   ...> select docid from Frequency WHERE term = 'world'   
   ...> INTERSECT
   ...> select docid from Frequency WHERE term = 'transactions'
   ...> );


#prob2:
# sqllite: .output stdout/list/line -->can show the column/row name;
# 


sqlite> select s from (
   ...> select a.row_num, b.col_num, sum(a.value * b.value) as s
   ...> from a, b
   ...> where a.col_num = b.row_num
   ...> group by a.row_num, b.col_num
   ...> )
   ...> where row_num=2 AND col_num=3
   ...> ;

## but hints is use "join" how to do that??

## prob3h:
sqlite> select d1.docid, d2.docid
   ...> from Frequency as d1, Frequency as d2
   ...> where d1.term = d2.term
   ...> group by d1.docid, d2.docid
   ...> ;

A X A
SELECT A1.row, A2.col
  FROM A AS A1, A AS A2
  WHERE A1.col = A2.row 
  GROUP BY A1.row, A2.col;

A X AT
SELECT A1.row, A2.row <-----change this
  FROM A AS A1, A AS A2
  WHERE A1.col = A2.col <----- change this
  GROUP BY A1.row, A2.row <-----change this
11

a.docid = '10080_txt_crude' and b.docid='17035_txt_earn'


$ time sqlite3 reuters.db < part8.sql > ../../Desktop/output.txt
real 119m0.539s
user 112m41.103s
sys 5m15.420s

## 3i:
Use the query like  document, and then compute the similarity of the query with every document, and find the max score.
