# Election Analysis - Vote Count Report
## Overview
This Election Audit analyzed results from the Congressional district election between three candidates across three counties (Denver, Jefferson, Arapahoe) to deliver the results about the turn out and winner. 

## Purpose
The purpose of this audit was to deliver a summary to the Colorado Board of Elections employee of the election results file that answered the below questions:

	1) What was the total amount of ballots cast in this election
	2) Who won the election, by what percentage, and with how many total votes
	3) What percentage and total votes did all candidates receive
	4) What percentage and total votes came from each county
	5) What county did most of the ballots come from

*Deliverables 1 and 2 below

## Results

### 1) What was the total amount of ballots cast in this election
The total amount of ballots cast in this election (Mail-In Ballots, Punch Cards, Memory Cards) was 369,711. 

![Deliverable3-1](/Resources/Deliverable3-1.png)

### 2) Who won the election, by what percentage, and with how many total votes
Diana DeGette won this election receiving 73.8% of the total votes or 272,892 votes. 

![Deliverable3-2](/Resources/Deliverable3-2.png)

### 3) What percentage and total votes did all candidates receive
The percentage of candidate votes were not split evenly. Diana lead with 73.8% of the total vote count, followed far behind by Charles Stockham with 23.0% and then trailing even farther behind by Raymon Doane with only 3% of the votes.

![Deliverable3-3](/Resources/Deliverable3-3.png)

### 4) What percentage and total votes came from each county
There were three counties that were represented in this election. The split between the three counties was very uneven with Jefferson and Arapahoe counties taking up less than 50% of the total votes combined. 

![Deliverable3-4](/Resources/Deliverable3-4.png)

### 5) What county did most of the ballots come from
Votes from Denver county made up the majority of the election results with 82.8% of the vote count (306,055).

![Deliverable3-5](/Resources/Deliverable3-5.png)

## Reusing this script 

## Why
Reusing this script will save time and resources if it is used in future elections in Colorado. This file should be saved and distributed to other teams working on elections across various type of elections in the area once the official counts are tabulated. 

## How
This script can be easily reused in any type of election because the variables are agnostic of this particular election. It acts as a shell for any data set organized the same way. 

### Example 1 -  
The variables that identify candidate and county are defined by column header (2 and 1 respectively). Therefore a file of the same organization can be swapped into this script and run using the same columns to determine the election results. 

Current: Candidate name in row 2, County name in row 1

![Deliverable3-6](/Resources/Deliverable3-6.png)

To be: flexible variable and rows

![Deliverable3-7](/Resources/Deliverable3-7.png)

To complete this update, you must be sure to update all mentioned of the original variables. Also, the script can be modified to adjust to the column number [1] [2] for the variable in questions per election.

### Example 2 - 
This script could also be modified to output a new data point: the percentage of …voters eligible in the district / how many voters actually voted in that district. This is advised to give a full picture of the % split between districts and advise how 

To do this you could utilize a dictionary to store the total eligible voters in each county. This should give you the percentage of turn out in each district.

![Deliverable3-8](/Resources/Deliverable3-8.png)


## Deliverable 1 and 2 screenshots

### Output to terminal

![Deliverable1](/Resources/Deliverable1.png)

### Output to file

![Deliverable2](/Resources/Deliverable2.png)
