# SWAPI Test

For this test I used the Python language to make requests to the SWAPI HTTP and get the starships data.

So after getting all starships data I was able to get the consumable and MGLT from all starships and calculate how many stops this starship would need to do before getting to the destination (any distance).

So, after getting the MGLT and consumable data I got the required hours to get to the destination by dividing the distance by MGLT.

With that, I could get how many days it would take to travel this distance.

Having those days I needed to convert the consumable data to days, and by that I converted months, years, weeks and days by multiplying the first value to their time (month = 30 *, year = 365 * and etc.)

After that all I needed to do was to divide this value by the number of days of travel, getting the number of stops necessary.

With the tests I was able to assert if the variables had the right type and if the list of starships had all the starships data.

