from pymongo import MongoClient

import pymongo

client = pymongo.MongoClient()

db=client["Movies"]

col = db["Movies"]

values=[{"_id":1,"Movie Name":"The Lion King","Director name":"Roger Allers","Actor name":"Matthew Broderick","Actress name":"Moira Kelly","Year of release":1994},
        {"_id":2,"Movie Name":"Lady and the Tramp","Director name":"Wilfred Jackson","Actor name":"Larry Roberts","Actress name":"Barbara Luddy","Year of release":1955},
        {"_id":3,"Movie Name":"Babys Day Out","Director name":"Patrick Read Johnson","Actor name":"Adam Robert Worton","Actress name":"Lara Flynn Boyle","Year of release":1994},
        {"_id":4,"Movie Name":"Charlie and the Chocolate Factory","Director name":"Tim Burton","Actor name":"Freddie Highmore","Actress name":"Helena Bonham Carter","Year of release":2005},
        {"_id":5,"Movie Name":"Ratatouille","Director name":"Brad Bird","Actor name":"Patton Oswalt","Actress name":"Janeane Garofalo","Year of release":2007},
        {"_id":6,"Movie Name":"The Incredibles","Director name":"Brad Bird","Actor name":"Craig T. Nelson","Actress name":"Holly Hunter","Year of release":2004},
        {"_id":7,"Movie Name":"Coco","Director name":"Lee Unkrich","Actor name":"Anthony Gonzalez","Actress name":"Alanna Ubach","Year of release":2017},
        {"_id":8,"Movie Name":"Toy Story","Director name":"John Lasseter","Actor name":"Tom Hanks","Actress name":"Annie Potts","Year of release":1995},
        {"_id":9,"Movie Name":"Kung Fu Panda","Director name":"Mark Osborne","Actor name":"Jack Black","Actress name":"Angelina Jolie","Year of release":2008},
        {"_id":10,"Movie Name":"101 Dalmations","Director name":"Stephen Herek","Actor name":"Jeff Daniels","Actress name":"Glenn Close","Year of release":1996},
        {"_id":11,"Movie Name":"A Bugs Life","Director name":"John Lasseter","Actor name":"Dave Foley","Actress name":"Hayden Panettiere","Year of release":1998},
        {"_id":12,"Movie Name":"Finding Nemo","Director name":"Andrew Stanton","Actor name":"Albert Brooks","Actress name":"Ellen DeGeneres","Year of release":2003},
        {"_id":13,"Movie Name":"Big Hero 6","Director name":"Don Hall","Actor name":"Ryan Potter","Actress name":"Jamie Chung","Year of release":2014},
        {"_id":14,"Movie Name":"Monsters Inc","Director name":"Pete Docter","Actor name":"John Goodman","Actress name":"Jennifer Tilly","Year of release":2001},
        {"_id":15,"Movie Name":"Onward","Director name":"Dan Scanlon","Actor name":"Tom Holland","Actress name":"Julia Louis-Dreyfus","Year of release":2020},
        {"_id":16,"Movie Name":"Inside Out","Director name":"Pete Docter","Actor name":"Richard Kind","Actress name":"Amy Poehler","Year of release":2015},
        {"_id":17,"Movie Name":"Frozen","Director name":"Jennifer Lee","Actor name":"Kristen Bell","Actress name":"Jonathan Groff","Year of release":2001},
        {"_id":18,"Movie Name":"Jurassic Park","Director name":"Steven Spielberg","Actor name":"Sam Neill","Actress name":"Laura Dern","Year of release":1993},
        {"_id":19,"Movie Name":"Dr. Dolittle","Director name":"Betty Thomas","Actor name":"Eddie Murphy","Actress name":"Kristen Wilson","Year of release":1998},
        {"_id":20,"Movie Name":"Home Alone","Director name":"Chris Columbus","Actor name":"Macaulay Culkin","Actress name":"Catherine O Hara","Year of release":2001}]
     

col.insert_many(values)

result=col.find()

for i in result:
    print(i)

query={"Director name":"Brad Bird"}

result=col.find(query)

for i in result:
    print(i)
