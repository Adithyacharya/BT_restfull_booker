Question:
----------------------------------
1. Generate 3 new bookings --> Log below scenarios to a log file
 All available booking ID's
 Above added 3 new booking details
2.      Modify total price for test1 to 1000 and test2 to 1500. Log this data to same log file.
3.      Delete one of the booking --> Log return status to same file
4.      Present the data in log file as html report.

---------------------------------------
Steps:
1. Clone/ download the repo into local machine.
2. Go to BT_heroku/data/test_data.json
    1. Initilize the 3 users data.
    Note: if not initilized it will take the current default value.
3. Go to BT_heroku/data/test_data.ini
        modify the below parameter as per the testcase for user1 and user2.
        Example 1:
       modify_totalprice = 1000
       depositpaid = True
       additionalneeds = Lunch
4. Launch the command prompt at BT_heroku
5. Create vitural env- python -m venv venv
6. Active the vitural env-
    MAC- source venv/bin/activate
    win- venv\Scripts\activate
7. Then install all the Dependencies from requirement file.- pip install -r requirements.txt
8. To run the testcases- pytest




