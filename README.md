## About

This project is a data wrangler aimed to create a clean and logical
representation for courses of the [Australian National University (ANU)](https://www.anu.edu.au/). Even
though much of the wrangling processes are automated, there is still a lot of manual wrangling work needed 
to format data such as course requirements and incompatibilities in a uniform, logical manner, while also
presenting special requirements, schedules, and other edge cases. Therefore, only computing courses and math courses
are wrangled. 

The aim of this project is to provide a representation for my future project: a web-based application in
ReactJS aimed to make timetabling easier for computing students of ANU, by creating an interface that
analyzes course requirements, incompatibilities, and interactive GUI. Without a consistent representation
of the data, there will be no way to accomplish that. 

## Logical Expressions

Due to the varying logical formulae used to represent course requisites, a uniform
way of expressing such logic is needed. Unfortunately, ANU does not have a concise, uniform
description thereof, and everything is conveyed through text. 

For example, this is the course requirements needed for the COMP3430 class:

> Students are required to have completed introductory courses on databases, programming and algorithms. 
To enrol in this course you must have completed
   6 units from COMP1030 or COMP1100 or COMP1130 or COMP1730; AND
   6 units from COMP1040 or COMP1110 or COMP1140; AND 
   COMP2400
Incompatible with COMP8430 and COMP8930.

Even though it is intuitive to simplify this into logical expressions such as
```
(COMP1030 OR COMP1100 OR COMP1130 OR COMP1730) AND (COMP1040 OR COMP1110 OR COMP1140) AND COMP2400
```

It is much easier to use a 2D array instead, where each row represent
a list of items with an OR relation, and every row has an AND relation to each other.

```json
[
   ["COMP1030", "COMP1100", "COMP1130", "COMP1730"],
   ["COMP1040", "COMP1110", "COMP1140"],
   ["COMP2400"]
]
```

To wrangle something like "Incompatible with COMP8430 and COMP8930", all we need to do is list the courses it is incompatible with
in a different key-value pair:

```json
{
  "incompatible": ["COMP8430", "COMP8930"] 
}
```