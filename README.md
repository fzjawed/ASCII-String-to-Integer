# ASCII-String-to-Integer

>14 June 2021 01:01 PM

So I did this last night but I fell asleep. Had to go the gym today 🏃‍♀️ I skipped 🏃‍♀️ 🏃‍♀️ I was so ready to go too idk man it's just difficult. 

I even fixed my playlist man - i rlly should go tomorrow

***Question: You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.***

So for this question the solution I came up is basically every time you approach a number you add it to a temp variable and then when you hit a letter you sum the int(temp) and store it in a variable called ``total``. Basically it's to make sure if there's two consecutive digits they're considered to be one number. 

In the v v end we're returning ``total += int(temp)`` - This is because the last digit will be stored in the int(temp) variable if the last position in the string is a digit. If not then temp will be 0 and will make no difference to the total.

I also found this super cool method using regex that I wanted to keep here. (creds given)

This map() function is so cool 🤠

``map(int, alpha.sub(" ", s)``

In the line above the map() takes ``int`` as sort of a function so basically what it'll do is convert all the values from the next argument into an integer. It's first argument can be any function and it'll just feed the next argument into that function and return a new iterable. 

``alpha.sub(" ", s)``

alpha is our regex - the ``.sub()`` is used to substitute all occurrences of the regex with space.

The solutions is super well explained [here](https://binarysearch.com/problems/ASCII-String-to-Integer/solutions/3667524)
