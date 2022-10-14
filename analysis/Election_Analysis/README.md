# Election_Analysis

### Overview of Election Audit 
The purpose of this audit, was to find the data, and report the total votes, the percentage of votes and the winner of the election of the counties of Jefferson, Denver and Arapahoe, also we have to report the information of the turnout for each county and the county with the biggest turnout. We used Visual Studio to read and analyze the information that was gaven to us in CSV file. With this, we created a program that helpes us to find what we wanted, and to send the information that we found, to a text file. This help Tom´s manager to automate the process for each election for now on. 

### Election-Audit Results
- How many votes were cast in this congressional election? There were cast 369,711 in all the counties. 
  ![image](https://user-images.githubusercontent.com/113566508/195477255-0bdd4a2a-8fdc-4228-9588-cac03f90da72.png)
  Here is the "for loop" we used to find the total of votes. 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. 
  ![image](https://user-images.githubusercontent.com/113566508/195477427-8ef5ee96-6dc2-4543-94b9-5bc5f493df6d.png)
  ![image](https://user-images.githubusercontent.com/113566508/195477565-7f616e6c-ba7a-4f7f-8481-7d615418f50b.png)
  This is how we found the information of the counties.
- Which county had the largest number of votes? Denver
  In the last image, in the bottom part, we have the if statement on how we manage to show the county with the most votes. 
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  ![image](https://user-images.githubusercontent.com/113566508/195477799-9fdbb6da-e453-4708-847d-a326cef9cb0b.png)
  ![image](https://user-images.githubusercontent.com/113566508/195477860-dd770510-4bf9-4c7b-a72d-4f387a55a7b5.png)
  Here is shown the for loop that we used to find this information on the candidates. 
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes? The winner is Diana DeGette with a total of 272,892 votes and with the 73.8%
  In the last image, in the bottom part, we have the if statement on how we manage to show the candidate who won the election.
  
 ### Summary 
 This program can be used to automate the results of every election we have in front. If we receive the CSV file in the same format (Ballot ID, County, Candidate), we just have to change the path to get the file where we are getting all the information. In case we receive the file with a differente format, we just need to make a minimal changes in order to get the results we want. 
 
 For example, the election commision, at the final stages of my work, asked me to add the vote information of each county, what I did I just took as a base what we had with the candidates program, and I changed some variables in order to get the county information. 
 
 Another example, would be if we move to another state, and for that reason we have new counties and off course new candidates. If we have this information in a new CSV file, we would just need to set the path to that document, and the program will do its magic. Even if we add more candidates, and more counties, the program will work as it is working now. 
 
 This program will help you automatize the process of getting the results for every election in the country! You just have to make a few changes, and run the program, and that is it! 
 
 

  
  
  



