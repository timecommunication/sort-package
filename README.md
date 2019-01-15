# sort-package
basic sort algorithms's performance
---

|          algorithm           | stability | is in-place sort |        time complexity        | space complexity |                             memo                             |
| :--------------------------: | :-------: | :--------------: | :---------------------------: | :--------------: | :----------------------------------------------------------: |
|        selection sort        |    no     |       yes        |         N<sup>2</sup>         |        1         |                                                              |
|        insertion sort        |    yes    |       yes        |        N~N<sup>2</sup>        |        1         |             depend on the distribution of input              |
|          shell sort          |    no     |       yes        | NlogN ?<br/>N<sup>6/5 </sup>? |        1         |                                                              |
|          quick sort          |    no     |       yes        |             NlogN             |       lgN        |   the operating efficiency is guaranted by the probability   |
| three-directional quick sort |    no     |       yes        |            N~NlogN            |       lgN        | the operating efficiency is guaranted by the probability,  and affected by the distribution of the input |
|          merge sort          |    yes    |        no        |             NlogN             |        N         |                                                              |
|          heap sort           |    no     |       yes        |             NlogN             |        1         |                                                              |
